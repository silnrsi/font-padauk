<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:svg="http://www.w3.org/2000/svg" xmlns:html='http://www.w3.org/1999/xhtml'>

<xsl:output method="xml" indent = "yes"/>

<xsl:param name="left"/>
<xsl:param name="right"/>

<xsl:template match="/">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="html:body">
<xsl:copy>
<xsl:apply-templates/>
<div id="key" style="border-width: 1px; border-style: solid; float: right;" title="Key">
<p>
Same glyphs, different positions:<br />
<span style="color:#a0a0a0">identical glyph positions</span><br />
<span style="color:#ff0000;"><xsl:value-of select="$left"/> glyph position</span><br />
<span style="color:#0000ff;"><xsl:value-of select="$right"/> glyph position</span><br />
Different glyphs:<br />
<span style="color:#ff00ff;"><xsl:value-of select="$left"/> glyphs</span><br />
<span style="color:#00ffff;"><xsl:value-of select="$right"/> glyphs</span>
</p>
</div>
</xsl:copy>
</xsl:template>


<xsl:template match="html:object">

<xsl:variable name="prefix" select="substring-before(@data,$right)"/>
<xsl:variable name="suffix" select="substring-after(@data,$right)"/>
<xsl:variable name="svg" select="document(concat('results/',$prefix,$left,$right,$suffix))"/>
<object type="{@type}" data="{concat($prefix,$left,$right,$suffix)}" width="{ceiling($svg/svg:svg/@width)}" height="{ceiling($svg/svg:svg/@height)}" alt="{@alt}" title="{@title}"/>

</xsl:template>

<xsl:template match="html:title">
<title>
<xsl:value-of select="substring-before(.,$right)"/>
<xsl:value-of select="concat($left,$right)"/>
</title>
</xsl:template>

<xsl:template match="@*|node()">
  <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
</xsl:template>


</xsl:stylesheet>
