<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:import href="padauk_common.xsl"/>

<xsl:template match="point[../@PSName='u1008.med' and @type='U']">
	<xsl:copy xml:space="preserve"><xsl:apply-templates select="@*"/>
		<location x="{location/@x}" y="{../../glyph[@PSName='u1009']/point[@type='U']/location/@y}"/>
	</xsl:copy>
</xsl:template>

</xsl:stylesheet>
