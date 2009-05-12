<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output indent="yes"/>
<xsl:param name="metricsFile"/>
<xsl:variable name="metrics" select="document($metricsFile)/font/glyphs"/>

<xsl:template match="glyph[contains(@PSName,'.med') or contains(@PSName,'u103D') or contains (@PSName,'u103E')]">
     <xsl:variable name="psName" select="@PSName"/>
    <xsl:copy><xsl:apply-templates select="@*"/>
        <xsl:variable name="shift" select="$metrics/glyph[@PSName=$psName]/@advance"/>
        <base PSName="{base/@PSName}">
        <xsl:choose><xsl:when test="$psName = 'u1008.med'"></xsl:when>
            <xsl:when test="$psName = 'u105B.med'"></xsl:when>
            <xsl:when test="$shift &gt; 0"><shift x="{-$shift}" y="0"/><advance width="0"/>
                <xsl:message terminate="no"><xsl:value-of select="$psName"/> 
                <xsl:value-of select="number($shift)"/></xsl:message>
            </xsl:when>
            <xsl:otherwise>
            </xsl:otherwise>
        </xsl:choose>
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
