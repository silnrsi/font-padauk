<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output indent="yes"/>
<xsl:param name="metricsFile"/>
<xsl:variable name="metrics" select="document($metricsFile)/font/glyphs"/>

<!-- Strip off the advances of marks, since there is inconsistent handling of the advance between
different OpenType implementations -->
<xsl:template match="glyph[contains(@PSName,'.med') or starts-with(@PSName,'u103D') or starts-with(@PSName,'u103E') or @PSName = 'u102D'  or @PSName = 'u102E' or @PSName = 'u1032' or @PSName = 'u1033' or @PSName = 'u1034' or @PSName = 'u1035' or @PSName = 'u1036' or @PSName = 'u105E' or @PSName = 'u105F' or @PSName = 'u1060' or @PSName = 'u1072' or @PSName = 'u1074' or @PSName = 'u1085' or @PSName = 'u1086' ]">
     <xsl:variable name="psName" select="@PSName"/>
     <xsl:variable name="psName2" select="base/@PSName"/>
    <xsl:copy><xsl:apply-templates select="@*"/>
        <xsl:variable name="shift" select="$metrics/glyph[@PSName=$psName]/@advance"/>
        <xsl:variable name="shift2" select="$metrics/glyph[@PSName=$psName2]/@advance"/>
        <xsl:element name="base">
        <xsl:if test="base/@PSName">
                <xsl:attribute name="PSName"><xsl:value-of select="base/@PSName"/></xsl:attribute>
        </xsl:if>
        <xsl:if test="base/@UID">
            <xsl:attribute name="UID"><xsl:value-of select="base/@UID"/></xsl:attribute>
        </xsl:if>
        <xsl:choose><xsl:when test="$psName = 'u1008.med'"></xsl:when>
            <xsl:when test="$psName = 'u105B.med'"></xsl:when>
            <xsl:when test="$shift2 &gt; 0"><shift x="{-$shift2}" y="0"/><advance width="1"/></xsl:when>
            <xsl:when test="$shift &gt; 0"><shift x="{-$shift}" y="0"/><advance width="0"/>
                <!-- <xsl:message terminate="no"><xsl:value-of select="$psName"/><xsl:text> </xsl:text> 
                <xsl:value-of select="number($shift)"/></xsl:message> -->
            </xsl:when>
            <xsl:otherwise>
            </xsl:otherwise>
        </xsl:choose>
        </xsl:element>
    </xsl:copy>
</xsl:template>

<!-- default copy template -->
<xsl:template match="@*|node()">
  <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
</xsl:template>


</xsl:stylesheet>
