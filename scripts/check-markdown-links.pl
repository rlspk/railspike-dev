#!/usr/bin/env perl

use strict;
use warnings;

use Cwd qw(getcwd abs_path);
use File::Basename qw(dirname);
use File::Find;
use File::Spec;

die "Usage: check-markdown-links.pl [ROOT [BASELINE]]\n" if @ARGV > 2;
my $root = abs_path(@ARGV ? shift @ARGV : getcwd());
die "Not a directory\n" unless defined($root) && -d $root;
my %baseline;
if (@ARGV) {
    open my $handle, '<', shift @ARGV or die "Cannot read baseline: $!\n";
    while (my $line = <$handle>) {
        next if $line =~ /^#/;
        $line =~ s/^\s+|\s+$//g;
        $baseline{$line} = 1 if length $line;
    }
    close $handle;
}
my %ignored_directories = map { $_ => 1 } qw(.git .idea node_modules);
my @markdown_files;

find(
    {
        no_chdir => 1,
        wanted   => sub {
            my $path = $File::Find::name;

            return if -l $path;
            if (-d $path) {
                $File::Find::prune = 1 if $ignored_directories{(File::Spec->splitdir($path))[-1]};
                return;
            }

            push @markdown_files, $path if -f $path && /\.md\z/;
        },
    },
    $root,
);

my @failures;
for my $file (@markdown_files) {
    open my $handle, '<', $file or die "Unable to read $file: $!\n";
    local $/;
    my $source = <$handle>;
    close $handle;

    while ($source =~ /\[[^\]]*\]\(([^)]+)\)/g) {
        my $original_target = $1;
        my $target = $original_target;
        $target =~ s/^\s+|\s+$//g;
        $target =~ s/^<(.*)>$/$1/s if $target =~ /^<.*>$/s;

        next if !$target
            || $target =~ /^#/
            || $target =~ /[{}]/
            || $target =~ /^(?:https?:|mailto:)/;

        $target =~ s/#.*\z//s;
        my $resolved = File::Spec->rel2abs($target, dirname($file));
        next if !$target || -e $resolved;

        push @failures, File::Spec->abs2rel($file, $root) . " -> $original_target";
    }
}

my %found = map { $_ => 1 } @failures;
my @known = grep { $found{$_} } keys %baseline;
my @stale = grep { !$found{$_} } keys %baseline;
@failures = grep { !$baseline{$_} } @failures;
push @failures, map { "Stale baseline entry: $_" } sort @stale;
print 'Acknowledged ' . scalar(@known) . " historical link targets from explicit baseline.\n" if @known;
if (@failures) {
    print STDERR "Broken local Markdown links:\n";
    print STDERR "- $_\n" for @failures;
    exit 1;
}

print 'Checked ' . scalar(@markdown_files) . " Markdown files: local links are valid.\n";
