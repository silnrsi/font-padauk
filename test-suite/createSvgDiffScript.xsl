<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:svg="http://www.w3.org/2000/svg" xmlns:html='http://www.w3.org/1999/xhtml'>

<xsl:output method="text"/>

<xsl:template match="/">

<xsl:for-each select="//html:object">
<xsl:variable name="prefix" select="substring-before(@data,'_icu')"/>
<xsl:variable name="suffix" select="substring-after(@data,'_icu')"/>

<xsl:text>xsltproc -o test-suite/results/</xsl:text>
<xsl:value-of select="$prefix"/><xsl:text>_icugr</xsl:text><xsl:value-of select="$suffix"/>
<xsl:text> --stringparam origSvg file:`pwd`/test-suite/tmp/</xsl:text>
<xsl:value-of select="$prefix"/><xsl:text>_icu</xsl:text><xsl:value-of select="$suffix"/>
<xsl:text> /usr/local/share/graphitesvg/diffSvg.xsl test-suite/tmp/</xsl:text>
<xsl:value-of select="$prefix"/><xsl:text>_gr</xsl:text><xsl:value-of select="$suffix"/>
<xsl:text>
</xsl:text>

<xsl:text>xsltproc -o test-suite/results/</xsl:text>
<xsl:value-of select="$prefix"/><xsl:text>_icuhb</xsl:text><xsl:value-of select="$suffix"/>
<xsl:text> --stringparam origSvg file:`pwd`/test-suite/tmp/</xsl:text>
<xsl:value-of select="$prefix"/><xsl:text>_icu</xsl:text><xsl:value-of select="$suffix"/>
<xsl:text> /usr/local/share/graphitesvg/diffSvg.xsl test-suite/tmp/</xsl:text>
<xsl:value-of select="$prefix"/><xsl:text>_hb</xsl:text><xsl:value-of select="$suffix"/>
<xsl:text>
</xsl:text>

</xsl:for-each>


</xsl:template>


</xsl:stylesheet>
