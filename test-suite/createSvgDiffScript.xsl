<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:svg="http://www.w3.org/2000/svg" xmlns:html='http://www.w3.org/1999/xhtml'>

<xsl:output method="text"/>
<xsl:param name="left"/>
<xsl:param name="right"/>
<xsl:param name="local"/>

<xsl:variable name="diffSvg">/usr/<xsl:value-of select="$local"/>share/graphitesvg/diffSvg.xsl</xsl:variable>

<xsl:template match="/">
<xsl:for-each select="//html:object">
<xsl:variable name="prefix" select="substring-before(@data,$right)"/>
<xsl:variable name="suffix" select="substring-after(@data,$right)"/>

<xsl:text>xsltproc -o test-suite/results/</xsl:text>
<xsl:value-of select="$prefix"/>
<xsl:value-of select="concat($left,$right)"/><xsl:value-of select="$suffix"/>
<xsl:text> --stringparam xTolerance 100 --stringparam origSvg file:`pwd`/test-suite/tmp/</xsl:text>
<xsl:value-of select="$prefix"/><xsl:value-of select="$right"/>
<xsl:value-of select="$suffix"/>
<xsl:text> </xsl:text><xsl:value-of select="$diffSvg"/><xsl:text> test-suite/tmp/</xsl:text>
<xsl:value-of select="$prefix"/><xsl:value-of select="$left"/>
<xsl:value-of select="$suffix"/>
<xsl:text>
</xsl:text>
</xsl:for-each>
</xsl:template>


</xsl:stylesheet>

