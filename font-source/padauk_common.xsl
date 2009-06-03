<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output indent="yes"/>
<xsl:param name="metricsFile"/>
<xsl:variable name="metrics" select="document($metricsFile)/font/glyphs"/>

<!-- add Fake attachments to prevent glyphs becoming marks in make_volt -->
<xsl:template match="glyph[@PSName='u1037'] |
                    glyph[@PSName='u1038'] |
                    glyph[@PSName='u1087'] |
                    glyph[@PSName='u1088'] |
                    glyph[@PSName='u1089'] |
                    glyph[@PSName='u108A'] |
                    glyph[@PSName='u108B'] |
                    glyph[@PSName='u108C']
                    ">
    <xsl:copy xml:space="preserve"><xsl:apply-templates select="@*"/>
        <point type="FAKE">
            <location x="0" y="0"/>
        </point>
    <xsl:apply-templates select="node()"/>
  </xsl:copy>
</xsl:template>

<!-- 
Add BD attachment as a copy of BS when this is not a mark (no _BS) and there is no existing BD 
This is needed for [narrow cons] U+1039 [wide cons]
-->
<xsl:template match="glyph[point/@type='BS']">
  <xsl:copy>
    <xsl:apply-templates select="@*"/>
    <xsl:choose>
        <xsl:when test="point[@type='BD']">
        </xsl:when>
        <xsl:when test="point[@type='_BS']">
        </xsl:when>
        <xsl:otherwise xml:space="preserve">
    <point type="BD"><xsl:comment>Copied from BS</xsl:comment>
        <location x="{point[@type='BS']/location/@x}" y="{point[@type='BS']/location/@y}"/>
    </point></xsl:otherwise>
    </xsl:choose>
    <xsl:apply-templates select="node()"/>
  </xsl:copy>
</xsl:template>

<xsl:template match="glyph[contains(@PSName,'.med') or contains(@PSName,'u103D') or contains (@PSName,'u103E')]">
<xsl:variable name="psName" select="@PSName"/>
<xsl:variable name="origWidth" select="$metrics/glyph[@PSName=$psName]/@advance"/>
<xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
    <xsl:if test="$origWidth &gt; 0">
    <property name='GDL_origWidth' value='{concat($origWidth, "m")}'/>
    </xsl:if>
</xsl:copy>
</xsl:template>

<!-- default copy template -->
<xsl:template match="@*|node()">
  <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
</xsl:template>

</xsl:stylesheet>
