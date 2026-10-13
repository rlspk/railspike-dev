#!/usr/bin/env node

import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { dirname, extname, join, relative, resolve } from 'node:path';

if (process.argv.length > 4) throw new Error('Usage: check-markdown-links.mjs [ROOT [BASELINE]]');
const root = resolve(process.argv[2] || process.cwd());
if (!statSync(root).isDirectory()) throw new Error(`Not a directory: ${root}`);
const baseline = new Set(process.argv[3]
  ? readFileSync(process.argv[3], 'utf8').split(/\r?\n/).filter(line => line.trim() && !line.startsWith('#')).map(line => line.trim())
  : []);
const ignoredDirectories = new Set(['.git', '.idea', 'node_modules']);
const markdownFiles = [];

function visit(directory) {
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!ignoredDirectories.has(entry.name)) visit(join(directory, entry.name));
    } else if (entry.isFile() && extname(entry.name) === '.md') {
      markdownFiles.push(join(directory, entry.name));
    }
  }
}

visit(root);

let failures = [];
for (const file of markdownFiles) {
  const source = readFileSync(file, 'utf8');
  for (const match of source.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)) {
    let target = match[1].trim();
    if (target.startsWith('<') && target.endsWith('>')) target = target.slice(1, -1);
    if (
      !target ||
      target.startsWith('#') ||
      target.includes('{') ||
      target.includes('}') ||
      /^(https?:|mailto:)/.test(target)
    ) {
      continue;
    }

    target = target.split('#', 1)[0];
    if (target && !existsSync(resolve(dirname(file), target))) {
      failures.push(`${relative(root, file)} -> ${match[1]}`);
    }
  }
}

const found = new Set(failures);
const known = [...baseline].filter(item => found.has(item));
const stale = [...baseline].filter(item => !found.has(item));
failures = failures.filter(item => !baseline.has(item));
failures.push(...stale.sort().map(item => `Stale baseline entry: ${item}`));
if (known.length) console.log(`Acknowledged ${known.length} historical link targets from explicit baseline.`);
if (failures.length) {
  console.error('Broken local Markdown links:');
  console.error(failures.map((failure) => `- ${failure}`).join('\n'));
  process.exitCode = 1;
} else {
  console.log(`Checked ${markdownFiles.length} Markdown files: local links are valid.`);
}
