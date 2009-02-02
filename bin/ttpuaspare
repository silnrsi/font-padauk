#!/usr/bin/perl

use Font::TTF::Font;

unless (defined $ARGV[1])
{
    die <<'EOT';
    ttpuaspare [-s hex] infile.ttf outfile.ttf
Adds PUA entries for all unencoded glyphs in a font. Skipping any that are
defined and looping back to U+E000 if it gets to the end of the PUA. Thence on
up into plane 15 if there is no space in the PUA.

 -s hex     specifies starting PUA code to start generating from [F000]
EOT
}

$opt_s ||= "F000";
$base = hex($opt_s);

$f = Font::TTF::Font->open($ARGV[0]) || die "Can't open font file $ARGV[0]";

@rev = $f->{'cmap'}->read->reverse;
$s = {};
$v = $f->{'OS/2'}->read;

$cmin = 0xFFFF;
$cmax = 0;

for ($i = 3; $i < $f->{'maxp'}{'numGlyphs'}; $i++)
{
    if ($rev[$i] != 0)
    {
        $cmin = $rev[$i] if ($rev[$i] < $cmin);
        $cmax = $rev[$i] if ($rev[$i] > $cmax);
        $s->{$rev[$i]} = $i;
        next;
    }
    
    do
    {
        $base++;
        $base = 0xE000 if ($base > 0xF0FF && $base < 0x10000);
        $base = 0xF0000 if ($base == hex($opt_s));      # we've come full circle
    } while (defined $c->{'val'}{$base});
    
    $s->{$base} = $i;
    $cmin = $base if ($base < $cmin);
    $cmax = $base if ($base > $cmax);
    
}

foreach $c (@{$f->{'cmap'}{'Tables'}})
{
    $c->{'val'} = $s if ($c->{'Platform'} == 0 || $c->{'Platform'} == 3
        || ($c->{'Platform'} == 2 && $c->{'Encoding'} == 1));
    $har_surr = 1 if ($c->{'Platform'} == 3 && $c->{'Encoding'} == 10);
}

if ($cmax > 0xFFFF)
{
    push (@{$f->{'cmap'}{'Tables'}}, {
        'Platform' => 3,
        'Encoding' => 10,
        'Ver' => 0,
        'Format' => 12,
        'val' => $s}) unless ($has_surr);

    my $has_uni_table;
    foreach $c (@{$f->{'cmap'}{'Tables'}})
    {
        if ($c->{'Platform'} == 0 && $c->{'Encoding'} == 0) 
        {
            $c->{'Format'} = 12;
            $has_uni_table = 1;
        }
    }
    push (@{$f->{'cmap'}{'Tables'}}, {
        'Platform' => 0,
        'Encoding' => 0,
        'Ver' => 0,
        'Format' => 12,
        'val' => $s}) unless ($has_uni_table);
}
        

$v->{'usFirstCharIndex'} = $cmin > 0xFFFF ? 0xFFFF : $cmin;
$v->{'usLastCharIndex'} = $cmax > 0xFFFF ? 0xFFFF : $cmax;

$f->out($ARGV[1]);
