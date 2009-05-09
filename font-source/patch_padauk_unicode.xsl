<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output indent="yes"/>
<xsl:param name="metricsFile"/>
<xsl:variable name="metrics" select="document($metricsFile)/font/glyphs"/>

<xsl:template match="glyph[contains(@PSName,'.med') or contains(@PSName,'u103D') or contains (@PSName,'u103E')]">
     <xsl:variable name="psName" select="@PSName"/>
    <xsl:copy xml:space="preserve"><xsl:apply-templates select="@*"/>
        <xsl:variable name="shift" select="$metrics/glyph[@PSName=$psName]/@advance"/>
        <xsl:message terminate="no"><xsl:value-of select="$psName"/> <xsl:value-of select="$metrics/glyph[@PSName=$psName]/@advance"/></xsl:message>
        <base PSName="{base/@PSName}">
            <xsl:if test="$shift &gt; 0">
            <shift x="{-$shift}" y="0"/>
            </xsl:if>
        </base>
    </xsl:copy>
</xsl:template>

<!-- default copy template -->
<xsl:template match="@*|node()">
  <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
</xsl:template>


</xsl:stylesheet>
