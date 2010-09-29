<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<!-- for the moment this is the same as the regular one -->
<xsl:import href="padauk_common.xsl"/>

<xsl:template match="point[@type = 'U' and ../@PSName='u1041']">
  <xsl:copy>
    <xsl:apply-templates select="@*"/>
    <location x='293' y='495'/>
  </xsl:copy>
</xsl:template>

</xsl:stylesheet>
