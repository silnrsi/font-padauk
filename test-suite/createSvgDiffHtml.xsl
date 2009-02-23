<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:svg="http://www.w3.org/2000/svg" xmlns:html='http://www.w3.org/1999/xhtml'>

<xsl:output method="xml" indent = "yes"/>

<xsl:param name="compare"/>

<xsl:template match="/">
<xsl:apply-templates/>
</xsl:template>


<xsl:template match="html:object">

<xsl:variable name="prefix" select="substring-before(@data,'_icu')"/>
<xsl:variable name="suffix" select="substring-after(@data,'_icu')"/>
<object type="{@type}" data="{concat($prefix,'_icu',$compare,$suffix)}" alt="{@alt}"/>

</xsl:template>

<xsl:template match="@*|node()">
  <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
</xsl:template>


</xsl:stylesheet>
