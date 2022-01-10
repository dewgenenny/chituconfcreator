import csv
import pprint


#define standard parameters for all imported resins:
# ToDo - this is currently the standard setings for a SATURN printer. ONLY THE SATURN CONFIG is therefore correct
# ToDo - need to add per printer default settings


__resin="normal"
antiAliasLevel="4"
bAntiAliasLevelEditable="0"
bAntiAliasing="1"
bBottomInnerOutterCircleOffsetEnable="0"
bBuildAreaOffsetEnable="0"
bDisplayCorrectEnable="0"
bImageBlur="1"
bImageBlurPixelEditable="1"
bImageMask="0"
bInnerOutterCircleOffsetEnable="0"
bLockXYSizeRatio="1"
bSurfaceRoughEditable="0"
bottomEdgeExposureMM="0"
bottomEdgeExposureTimeS="4"
bottomExposureTimeStrategy="0"
bottomInnerCircleOffset="0"
bottomLayerCount="5"
bottomLayerDropHeight2="0"
bottomLayerDropSpeed="210"
bottomLayerDropSpeed2="0"
bottomLayerLiftHeight="7"
bottomLayerLiftHeight2="0"
bottomLayerLiftSpeed="70"
bottomLayerLiftSpeed2="0"
bottomLightIntensityPWM="255"
bottomLightOffTime="0"
bottomOutterCircleOffset="0"
bottomRestTimeAfterLift="0"
bottomRestTimeAfterRetract="0.5"
bottomRestTimeBeforeLift="0"
buildAreaOffsetBottom="0"
buildAreaOffsetLeft="0"
buildAreaOffsetRight="0"
buildAreaOffsetTop="0"
circleParityDifference="0"
currProfileName="Profile"
displayCorrectLeftBottomX="0"
displayCorrectLeftBottomY="0"
displayCorrectLeftTopX="0"
displayCorrectLeftTopY="0"
displayCorrectRightBottomX="0"
displayCorrectRightBottomY="0"
displayCorrectRightTopX="0"
displayCorrectRightTopY="0"
edgeExposureMM="0"
edgeExposureTimeS="4"
endGcode='""'
fillDensity="30"
fillPattern="None"
imageBlurPixel="2"
imageMaskFile=""
innerCircleOffset="0"
layerGcode='""'
layerHeight="0.05"
lightOffTime="8.5"
machineDepth="120"
machineHeight="200"
machineType="ELEGOO SATURN"
machineWidth="192"
maskGrayScaleUnit="4"
maxGreyLevel="255"
minGreyLevel="95"
normalLayerDropHeight2="0"
normalLayerDropSpeed="210"
normalLayerDropSpeed2="0"
normalLayerLiftHeight="7"
normalLayerLiftHeight2="0"
normalLayerLiftSpeed="70"
normalLayerLiftSpeed2="0"
normalLightIntensityPWM="255"
normalRestTimeAfterLift="0"
normalRestTimeAfterRetract="0.5"
normalRestTimeBeforeLift="0"
outterCircleOffset="0"
printWaitMode="0"
projectType="LCD_mirror"
resinDensity="1.1"
resinPrice="30"
resinUnit="$/L"
resolutionX="3840"
resolutionY="2400"
shellThickness="1.2"
sliceExportPart="0"
startGcode='""'
surfaceRoughLevel="1"
transitionLayerCount="10"
transitionLayerType="0"
zSlowUpDistance="0"

all_settings = {}
counter = 0
pp = pprint.PrettyPrinter(indent=4)

with open('google_sheets_export.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        model = row['3DP Model\r\n']
        resin_brand = row['Resin Brand\r\n']
        resin_type = row['Resin Type\r\n']
        color = row['Color\r\n']
        bottom_exposures = row['Bottom Exposure(s)\r\n']
        normal_exposures = row['Normal Exposure(s)\r\n']
        layer_height = row['Layer Height(mm)\r\n']

        profile_title = "@@" + resin_brand + " " + resin_type + "(" + color + ")@@"

        all_settings[counter] = {"profile_title": profile_title, "bottom_exposures": bottom_exposures,"normal_exposures": normal_exposures,"layer_height": layer_height}
        with open(model+".cfg", "a") as myfile:

            myfile.write(profile_title + "layerHeight:" + layerHeight + "\n")
            myfile.write(profile_title + "normal_exposures:" + normal_exposures + "\n")
            myfile.write(profile_title + "bottom_exposures:" + bottom_exposures + "\n")

            myfile.write(profile_title  + "__resin:"+ __resin + "\n")
            myfile.write(profile_title  + "antiAliasLevel:"+antiAliasLevel+ "\n" )
            myfile.write(profile_title  + "bAntiAliasLevelEditable:"+ bAntiAliasLevelEditable+ "\n" )
            myfile.write(profile_title  + "bAntiAliasing:" + bAntiAliasing + "\n" )
            myfile.write(profile_title  + "bBottomInnerOutterCircleOffsetEnable:" + bBottomInnerOutterCircleOffsetEnable + "\n" )
            myfile.write(profile_title  + "bBuildAreaOffsetEnable:"+ bBuildAreaOffsetEnable + "\n" )
            myfile.write(profile_title  + "bDisplayCorrectEnable:" + bDisplayCorrectEnable + "\n")

            myfile.write(profile_title  + "bImageBlur:" + bImageBlur + "\n")
            myfile.write(profile_title  + "bImageBlurPixelEditable:" + bImageBlurPixelEditable + "\n")
            myfile.write(profile_title  + "bImageMask:" + bImageMask + "\n")
            myfile.write(profile_title  + "bInnerOutterCircleOffsetEnable:" + bInnerOutterCircleOffsetEnable + "\n")
            myfile.write(profile_title  + "bLockXYSizeRatio:" + bLockXYSizeRatio + "\n")
            myfile.write(profile_title  + "bSurfaceRoughEditable:" + bSurfaceRoughEditable + "\n")
            myfile.write(profile_title  + "bottomEdgeExposureMM:" + bottomEdgeExposureMM + "\n")
            myfile.write(profile_title  + "bottomEdgeExposureTimeS:" + bottomEdgeExposureTimeS + "\n")
            myfile.write(profile_title  + "bottomExposureTimeStrategy:" + bottomExposureTimeStrategy + "\n")
            myfile.write(profile_title  + "bottomInnerCircleOffset:" + bottomInnerCircleOffset + "\n")
            myfile.write(profile_title  + "bottomLayerCount:" + bottomLayerCount + "\n")
            myfile.write(profile_title  + "bottomLayerDropHeight2:" + bottomLayerDropHeight2 + "\n")
            myfile.write(profile_title  + "bottomLayerDropSpeed:" + bottomLayerDropSpeed + "\n")
            myfile.write(profile_title  + "bottomLayerLiftHeight:" + bottomLayerLiftHeight + "\n")
            myfile.write(profile_title  + "bottomLayerLiftHeight2:" + bottomLayerLiftHeight2 + "\n")
            myfile.write(profile_title  + "bottomLayerLiftSpeed:" + bottomLayerLiftSpeed + "\n")
            myfile.write(profile_title  + "bottomLayerLiftSpeed2:" + bottomLayerLiftSpeed2 + "\n")
            myfile.write(profile_title  + "bottomLightIntensityPWM:" + bottomLightIntensityPWM + "\n")
            myfile.write(profile_title  + "bottomLightOffTime:" + bottomLightOffTime + "\n")
            myfile.write(profile_title  + "bottomOutterCircleOffset:" + bottomOutterCircleOffset + "\n")
            myfile.write(profile_title  + "bottomRestTimeAfterLift:" + bottomRestTimeAfterLift + "\n")
            myfile.write(profile_title  + "bottomRestTimeAfterRetract:" + bottomRestTimeAfterRetract + "\n")
            myfile.write(profile_title  + "bottomRestTimeBeforeLift:" + bottomRestTimeBeforeLift + "\n")
            myfile.write(profile_title  + "buildAreaOffsetBottom:" + buildAreaOffsetBottom + "\n")
            myfile.write(profile_title  + "buildAreaOffsetLeft:" + buildAreaOffsetLeft + "\n")
            myfile.write(profile_title  + "buildAreaOffsetRight:" + buildAreaOffsetRight + "\n")
            myfile.write(profile_title  + "buildAreaOffsetTop:" + buildAreaOffsetTop + "\n")
            myfile.write(profile_title  + "circleParityDifference:" + circleParityDifference + "\n")
            myfile.write(profile_title  + "currProfileName:" + currProfileName + "\n")
            myfile.write(profile_title  + "displayCorrectLeftBottomX:" + displayCorrectLeftBottomX + "\n")
            myfile.write(profile_title  + "displayCorrectLeftBottomY:" + displayCorrectLeftBottomY + "\n")
            myfile.write(profile_title  + "displayCorrectLeftTopX:" + displayCorrectLeftTopX + "\n")
            myfile.write(profile_title  + "displayCorrectLeftTopY:" + displayCorrectLeftTopY + "\n")
            myfile.write(profile_title  + "displayCorrectRightBottomX:" + displayCorrectRightBottomX + "\n")
            myfile.write(profile_title  + "displayCorrectRightBottomY:" + displayCorrectRightBottomY + "\n")
            myfile.write(profile_title  + "displayCorrectRightTopX:" + displayCorrectRightTopX + "\n")
            myfile.write(profile_title  + "displayCorrectRightTopY:" + displayCorrectRightTopY + "\n")
            myfile.write(profile_title  + "edgeExposureMM:" + edgeExposureMM + "\n")
            myfile.write(profile_title  + "edgeExposureTimeS:" + edgeExposureTimeS + "\n")
            myfile.write(profile_title  + "endGcode:" + endGcode + "\n")
            myfile.write(profile_title  + "fillDensity:"+ fillDensity + "\n")
            myfile.write(profile_title  + "fillPattern:" + fillPattern + "\n")
            myfile.write(profile_title  + "imageBlurPixel:" + imageBlurPixel + "\n")
            myfile.write(profile_title  + "imageMaskFile:" + imageMaskFile + "\n")
            myfile.write(profile_title  + "innerCircleOffset:" + innerCircleOffset + "\n")
            myfile.write(profile_title  + "layerGcode:" + layerGcode + "\n")
            #myfile.write(profile_title  + "layerHeight:" + layerHeight
            myfile.write(profile_title  + "lightOffTime:" + lightOffTime + "\n")
            myfile.write(profile_title  + "machineDepth:" + machineDepth + "\n")
            myfile.write(profile_title  + "machineHeight:" + machineHeight + "\n")
            myfile.write(profile_title  + "machineType:" + machineType + "\n")
            myfile.write(profile_title  + "machineWidth:" + machineWidth + "\n")
            myfile.write(profile_title  + "maskGrayScaleUnit:" + maskGrayScaleUnit + "\n")
            myfile.write(profile_title  + "maxGreyLevel:" + maxGreyLevel + "\n")
            myfile.write(profile_title  + "minGreyLevel:" + minGreyLevel + "\n")
            myfile.write(profile_title  + "normalLayerDropHeight2:" + normalLayerDropHeight2 + "\n")
            myfile.write(profile_title  + "normalLayerDropSpeed:" + normalLayerDropSpeed + "\n")
            myfile.write(profile_title  + "normalLayerDropSpeed2:" + normalLayerDropSpeed2 + "\n")
            myfile.write(profile_title  + "normalLayerLiftHeight:" + normalLayerLiftHeight + "\n")
            myfile.write(profile_title  + "normalLayerLiftHeight2:" + normalLayerLiftHeight2 + "\n")
            myfile.write(profile_title  + "normalLayerLiftSpeed:" + normalLayerLiftSpeed + "\n")
            myfile.write(profile_title  + "normalLayerLiftSpeed2:" + normalLayerLiftSpeed2 + "\n")
            myfile.write(profile_title  + "normalLightIntensityPWM:" + normalLightIntensityPWM + "\n")
            myfile.write(profile_title  + "normalRestTimeAfterLift:" + normalRestTimeAfterLift + "\n")
            myfile.write(profile_title  + "normalRestTimeAfterRetract:" + normalRestTimeAfterRetract + "\n")
            myfile.write(profile_title  + "normalRestTimeBeforeLift:" + normalRestTimeBeforeLift + "\n")
            myfile.write(profile_title  + "outterCircleOffset:" + outterCircleOffset + "\n")
            myfile.write(profile_title  + "printWaitMode:" + printWaitMode + "\n")
            myfile.write(profile_title  + "projectType:" + projectType + "\n")
            myfile.write(profile_title  + "resinDensity:" + resinDensity + "\n")
            myfile.write(profile_title  + "resinPrice:" + resinPrice + "\n")
            myfile.write(profile_title  + "resinUnit:" + resinUnit + "\n")
            myfile.write(profile_title  + "resolutionX:" + resolutionX + "\n")
            myfile.write(profile_title  + "resolutionY:" + resolutionY + "\n")
            myfile.write(profile_title  + "shellThickness:" + shellThickness + "\n")
            myfile.write(profile_title  + "sliceExportPart:" + sliceExportPart + "\n")
            myfile.write(profile_title  + "startGcode:" + startGcode + "\n")
            myfile.write(profile_title  + "surfaceRoughLevel:" + surfaceRoughLevel + "\n")
            myfile.write(profile_title  + "transitionLayerCount:" + transitionLayerCount + "\n")
            myfile.write(profile_title  + "transitionLayerType:" + transitionLayerType + "\n")
            myfile.write(profile_title  + "zSlowUpDistance:" + zSlowUpDistance + "\n")
            myfile.close()

        counter = counter + 1

