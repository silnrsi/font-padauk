<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<!-- for the moment this is the same as the regular one -->
<xsl:import href="padauk_common.xsl"/>

<xsl:template match="glyph[@PSName='u1065']">
<xsl:copy>
    <xsl:apply-templates select="@*"/>
    <point type='_R'>
            <location x='0' y='0'/>
    </point>
    <xsl:apply-templates select="node()"/>
</xsl:copy>
</xsl:template>

</xsl:stylesheet>
