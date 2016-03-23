#MenuTitle: Glyphs.app Unit Tests
# -*- coding: utf-8 -*-

#import GlyphsApp
#reload(GlyphsApp) 

import unittest

import GlyphsApp
from GlyphsApp import *
import os, time

PathToTestFile = os.path.join(os.path.dirname(__file__), 'Glyphs Unit Test Sans.glyphs')

class GlyphsAppTests(unittest.TestCase):
	
	def assertString(self, stringObject, assertType = True, readOnly = False):
		if assertType:
			self.assertIsInstance(str(stringObject), str)
		if readOnly == False:
			oldValue = stringObject
			stringObject = 'a'
			self.assertEqual(stringObject, 'a')
			stringObject = oldValue
	
	def assertDict(self, dictObject, assertType = True):
		if assertType:
			self.assertIsInstance(dict(dictObject), dict)
		var1 = 'abc'
		var2 = 'def'
		dictObject['uniTestValue'] = var1
		self.assertEqual(dictObject['uniTestValue'], var1)
		dictObject['uniTestValue'] = var2
		self.assertEqual(dictObject['uniTestValue'], var2)
	
	def assertInteger(self, intObject, assertType = True, readOnly = False):
		if assertType:
			assert type(int(intObject)) == int
		if readOnly == False:
			oldValue = intObject
			intObject = 1
			self.assertEqual(intObject, 1)
			intObject = oldValue
	
	def assertFloat(self, floatObject, assertType = True, readOnly = False):
		if assertType:
			self.assertIsInstance(float(floatObject), float)
		if readOnly == False:
			oldValue = floatObject
			floatObject = .5
			self.assertEqual(floatObject, .5)
			floatObject = oldValue
	
	def assertUnicode(self, unicodeObject, assertType = True, readOnly = False):
		if assertType:
			assert unicode(unicodeObject)
		if readOnly == False:
			oldValue = unicodeObject
			unicodeObject = u'Ə'
			self.assertEqual(unicodeObject, u'Ə')
			unicodeObject = oldValue
	
	def assertBool(self, boolObject, assertType = True, readOnly = False):
		if assertType:
			assert type(boolObject) == bool
		if readOnly == False:
			oldValue = boolObject
			boolObject = not boolObject
			self.assertEqual(boolObject, (not oldValue))
			boolObject = oldValue
	
	def setUp(self):
		Glyphs.clearLog()
	
	def tearDown(self):
		Glyphs.showMacroWindow()
	
	def test_GSApplication(self):
		
		# Main object
		self.assertIsNotNone(Glyphs)
		self.assertIsNotNone(Glyphs.__repr__())
		
		# close all fonts
		for font in Glyphs.fonts:
			font.close()
		
		# open font
		Glyphs.open(PathToTestFile)
		
		# Macro window
		Glyphs.showMacroWindow()
		
		# Assert font
		self.assertIsNotNone(Glyphs.font)
		self.assertEqual(len(Glyphs.fonts), 1)
		
		
		## Attributes
		
		# GSApplication.reporters
		self.assertGreater(len(list(Glyphs.reporters)), 0)
		self.assertGreater(len(Glyphs.reporters), 0)
		
		# activate all reporters
		
		for reporter in Glyphs.reporters:
			Glyphs.activateReporter(reporter)
		
		self.assertEqual(len(Glyphs.activeReporters), len(Glyphs.reporters))
		# deactivate all reporters
		for reporter in Glyphs.reporters:
			Glyphs.deactivateReporter(reporter)
		self.assertEqual(len(Glyphs.activeReporters), 0)
		
		# GSApplication.defaults
		self.assertDict(Glyphs.defaults, assertType = False)
		
		# GSApplication.scriptAbbrevations
		self.assertIsNotNone(dict(Glyphs.scriptAbbrevations))
		
		# GSApplication.scriptSuffixes
		self.assertIsNotNone(dict(Glyphs.scriptSuffixes))
		
		# GSApplication.languageScripts
		self.assertIsNotNone(dict(Glyphs.languageScripts))
		
		# GSApplication.languageData
		self.assertIsNotNone(list(map(dict, Glyphs.languageData)))
		
		# GSApplication.unicodeRanges
		self.assertIsNotNone(list(Glyphs.unicodeRanges))
		
		# GSApplication.editViewWidth
		self.assertInteger(Glyphs.editViewWidth)
		
		# GSApplication.handleSize
		self.assertInteger(Glyphs.handleSize)
		
		# GSApplication.versionString
		self.assertString(Glyphs.versionString, readOnly = True)
		
		# GSApplication.versionNumber
		self.assertFloat(Glyphs.versionNumber, readOnly = True)
		
		# GSApplication.buildNumber
		self.assertInteger(Glyphs.buildNumber, readOnly = True)
		
		## Methods
		
		# GSApplication.showGlyphInfoPanelWithSearchString()
		Glyphs.showGlyphInfoPanelWithSearchString('a')
		
		# GSApplication.glyphInfoForName()
		self.assertEqual(str(Glyphs.glyphInfoForName('a')), "<GSGlyphInfo 'a'>")
		
		# GSApplication.glyphInfoForUnicode()
		self.assertEqual(str(Glyphs.glyphInfoForUnicode('0061')), "<GSGlyphInfo 'a'>")
		
		# GSApplication.niceGlyphName()
		self.assertEqual(Glyphs.niceGlyphName('a'), 'a')
		
		# GSApplication.productionGlyphName()
		self.assertEqual(Glyphs.productionGlyphName('a'), 'a')
		
		# GSApplication.ligatureComponents()
		self.assertEqual(len(list(Glyphs.ligatureComponents('allah-ar'))), 4)
		
		# GSApplication.redraw()
		Glyphs.redraw()
		
		# GSApplication.showNotification()
		Glyphs.showNotification('Glyphs Unit Test', 'Hello World')
		
		self.assertIsNotNone(Glyphs.localize({
			'en':  'Hello World',
			'de': u'Hallöle Welt',
			'fr':  'Bonjour tout le monde',
			'es':  'Hola Mundo',
			}))


	def test_GSFont(self):
		
		font = Glyphs.font
		self.assertIsNotNone(font.__repr__())
		
		## Attributes
		
		# GSFont.parent
		self.assertIn('GSDocument', str(font.parent))
		
		# GSFont.masters
		self.assertGreaterEqual(len(list(font.masters)), 1)
		
		# GSFont.instances
		self.assertGreaterEqual(len(list(font.instances)), 1)
		
		# GSFont.glyphs
		self.assertGreaterEqual(len(list(font.glyphs)), 1)
		
		# GSFont.classes
		font.classes = []
		self.assertEqual(len(font.classes), 0)
		font.classes.append(GlyphsApp.GSClass('uppercaseLetters', 'A'))
		self.assertIsNotNone(font.classes['uppercaseLetters'].__repr__())
		self.assertEqual(len(font.classes), 1)
		self.assertIn('uppercaseLetters', str(font.classes))
		self.assertIn('A', font.classes['uppercaseLetters'].code)
		del(font.classes['uppercaseLetters'])
		self.assertEqual(len(font.classes), 0)
		
		# GSFont.features
		font.features = []
		self.assertEqual(len(font.features), 0)
		font.features.append(GlyphsApp.GSFeature('liga', 'sub f i by fi;'))
		self.assertIsNotNone(font.features['liga'].__repr__())
		self.assertEqual(len(font.features), 1)
		self.assertIn('<GSFeature "liga">', str(font.features))
		self.assertIn('sub f i by fi;', font.features['liga'].code)
		del(font.features['liga'])
		self.assertEqual(len(font.features), 0)
		
		# GSFont.featurePrefixes
		font.featurePrefixes = []
		self.assertEqual(len(font.featurePrefixes), 0)
		font.featurePrefixes.append(GlyphsApp.GSFeaturePrefix('LanguageSystems', 'languagesystem DFLT dflt;'))
		self.assertIsNotNone(font.featurePrefixes['LanguageSystems'].__repr__())
		self.assertEqual(len(font.featurePrefixes), 1)
		self.assertIn('LanguageSystems', str(font.featurePrefixes))
		self.assertIn('languagesystem DFLT dflt;', font.featurePrefixes['LanguageSystems'].code)
		del(font.featurePrefixes['LanguageSystems'])
		self.assertEqual(len(font.featurePrefixes), 0)
		
		# GSFont.copyright
		self.assertUnicode(font.copyright)
		
		# GSFont.designer
		self.assertUnicode(font.designer)
		
		# GSFont.designerURL
		self.assertUnicode(font.designerURL)
		
		# GSFont.manufacturer
		self.assertUnicode(font.manufacturer)
		
		# GSFont.manufacturerURL
		self.assertUnicode(font.manufacturerURL)
		
		# GSFont.versionMajor
		self.assertInteger(font.versionMajor)
		
		# GSFont.versionMinor
		self.assertInteger(font.versionMinor)
		
		# GSFont.date
		self.assertIsInstance(font.date, NSDate)
		
		# GSFont.familyName
		self.assertUnicode(font.familyName)
		
		# GSFont.upm
		self.assertInteger(font.upm)
		
		# GSFont.note
		self.assertUnicode(font.note)
		
		# GSFont.kerning
		self.assertIsInstance(dict(font.kerning), dict)
		
		# GSFont.userData
		self.assertDict(font.userData)
		
		# GSFont.disablesNiceNames
		self.assertBool(font.disablesNiceNames)
		
		# GSFont.customParameters
		font.customParameters['trademark'] = 'ThisFont is a trademark by MyFoundry.com'
		self.assertGreaterEqual(len(list(font.customParameters)), 1)
		del(font.customParameters['trademark'])
		
		# GSFont.grid
		self.assertInteger(font.grid)
		
		# GSFont.gridSubDivisions
		self.assertInteger(font.gridSubDivisions)
		
		# GSFont.gridLength
		self.assertFloat(font.gridLength, readOnly = True)
		
		# GSFont.selection
		for glyph in font.glyphs:
			glyph.selected = False
		font.glyphs['a'].selected = True
		self.assertEqual(len(list(font.selection)), 1)
		for glyph in font.glyphs:
			glyph.selected = True
		self.assertEqual(len(list(font.selection)), len(font.glyphs))
		
		# GSFont.selectedLayers
		# GSFont.currentText
		# GSFont.tabs
		# GSFont.currentTab
		for tab in font.tabs:
			tab.close()
		font.newTab('a')
		self.assertIsNotNone(font.currentTab.__repr__())
		self.assertEqual(len(list(font.selectedLayers)), 1)
		self.assertEqual(len(list(font.tabs)), 1)
		self.assertEqual(font.currentText, 'a')
		self.assertEqual(font.currentTab, font.tabs[-1])
		font.tabs[0].close()
		
		# GSFont.selectedFontMaster
		# GSFont.masterIndex
		oldMasterIndex = font.masterIndex
		for i in range(len(list(font.masters))):
			font.masterIndex = i
			self.assertEqual(font.selectedFontMaster, font.masters[i])
		font.masterIndex = oldMasterIndex
		
		# GSFont.filepath
		self.assertIsNotNone(font.filepath)
		
		# GSFont.tool
		# GSFont.tools
		oldTool = font.tool
		for toolName in font.tools:
			font.tool = toolName
			self.assertEqual(font.tool, toolName)
		font.tool = oldTool
		
		
		## Methods
		
		# GSFont.save()
		font.save()
		
		# GSFont.close()
		font.close()
		Glyphs.open(PathToTestFile)
		
		# GSFont.disableUpdateInterface()
		font.disableUpdateInterface()
		
		# GSFontselfenableUpdateInterface()
		font.enableUpdateInterface()
		
		# GSFont.setKerningForPair()
		font.setKerningForPair(font.masters[0].id, 'a', 'a', -10)
		
		# GSFont.kerningForPair()
		self.assertEqual(font.kerningForPair(font.masters[0].id, 'a', 'a'), -10)
		
		# GSFont.removeKerningForPair()
		font.removeKerningForPair(font.masters[0].id, 'a', 'a')


	def test_GSFontMaster(self):
		
		master = Glyphs.font.masters[0]
		self.assertIsNotNone(master.__repr__())
		
		# GSFontMaster.id
		self.assertIsNotNone(unicode(master.id))
		
		# GSFontMaster.name
		self.assertIsNotNone(str(master.name))
		self.assertIsNotNone(master.name)
		# GSFontMaster.weight
		self.assertIsNotNone(str(master.weight))
		
		# GSFontMaster.width
		self.assertIsNotNone(str(master.width))
		
		# GSFontMaster.weightValue
		self.assertFloat(master.weightValue)
		
		# GSFontMaster.widthValue
		self.assertFloat(master.widthValue)
		
		# GSFontMaster.customName
		self.assertString(master.customName)
		
		# GSFontMaster.customValue
		self.assertFloat(master.customValue)
		
		# GSFontMaster.ascender
		self.assertFloat(master.ascender)
		
		# GSFontMaster.capHeight
		self.assertFloat(master.capHeight)
		
		# GSFontMaster.xHeight
		self.assertFloat(master.xHeight)
		
		# GSFontMaster.descender
		self.assertFloat(master.descender)
		
		# GSFontMaster.italicAngle
		self.assertFloat(master.italicAngle)
		
		# GSFontMaster.verticalStems
		oldStems = master.verticalStems
		master.verticalStems = [10, 15, 20]
		self.assertEqual(len(list(master.verticalStems)), 3)
		master.verticalStems = oldStems
		
		# GSFontMaster.horizontalStems
		oldStems = master.horizontalStems
		master.horizontalStems = [10, 15, 20]
		self.assertEqual(len(list(master.horizontalStems)), 3)
		master.horizontalStems = oldStems
		
		# GSFontMaster.alignmentZones
		self.assertIsInstance(list(master.alignmentZones), list)
		
		# GSFontMaster.blueValues
		self.assertIsInstance(list(master.blueValues), list)
		
		# GSFontMaster.otherBlues
		self.assertIsInstance(list(master.otherBlues), list)
		
		# GSFontMaster.guides
		self.assertIsInstance(list(master.guides), list)
		master.guides = []
		self.assertEqual(len(master.guides), 0)
		newGuide = GSGuideLine()
		newGuide.position = NSPoint(100, 100)
		newGuide.angle = -10.0
		master.guides.append(newGuide)
		self.assertIsNotNone(master.guides[0].__repr__())
		self.assertEqual(len(master.guides), 1)
		del master.guides[0]
		self.assertEqual(len(master.guides), 0)

		
		# GSFontMaster.userData
		self.assertDict(master.userData)
		
		# GSFontMaster.customParameters
		master.customParameters['trademark'] = 'ThisFont is a trademark by MyFoundry.com'
		self.assertGreaterEqual(len(list(master.customParameters)), 1)
		del(master.customParameters['trademark'])
	
	def test_GSAlignmentZone(self):
		
		master = Glyphs.font.masters[0]
		
		master.alignmentZones = []
		self.assertEqual(len(master.alignmentZones), 0)
		master.alignmentZones.append(GlyphsApp.GSAlignmentZone(100, 10))
		self.assertIsNotNone(master.alignmentZones[-1].__repr__())
		self.assertEqual(len(master.alignmentZones), 1)
		self.assertEqual(master.alignmentZones[-1].position, 100)
		self.assertEqual(master.alignmentZones[-1].size, 10)
		del master.alignmentZones[-1]
		self.assertEqual(len(master.alignmentZones), 0)
	
	def test_GSInstance(self):
		
		instance = Glyphs.font.instances[0]
		self.assertIsNotNone(instance.__repr__())
		
		# GSInstance.active
		self.assertBool(instance.active, readOnly = True)
		
		# GSInstance.name
		self.assertString(instance.name)
		
		# GSInstance.weight
		self.assertString(instance.weight, readOnly = True)
		
		# GSInstance.width
		self.assertString(instance.width, readOnly = True)
		
		# GSInstance.weightValue
		self.assertFloat(instance.weightValue)
		
		# GSInstance.widthValue
		self.assertFloat(instance.widthValue)
		
		# GSInstance.customValue
		self.assertFloat(instance.customValue)
		
		# GSInstance.isItalic
		self.assertBool(instance.isItalic)
		
		# GSInstance.isBold
		self.assertBool(instance.isBold)
		
		# GSInstance.linkStyle
		self.assertString(instance.linkStyle)
		
		# GSInstance.familyName
		self.assertString(instance.familyName)
		
		# GSInstance.preferredFamily
		self.assertString(instance.preferredFamily)
		
		# GSInstance.preferredSubfamilyName
		self.assertString(instance.preferredSubfamilyName)
		
		# GSInstance.windowsFamily
		self.assertString(instance.windowsFamily)
		
		# GSInstance.windowsStyle
		self.assertString(instance.windowsStyle)
		
		# GSInstance.windowsLinkedToStyle
		self.assertString(instance.windowsLinkedToStyle)
		
		# GSInstance.fontName
		self.assertString(instance.fontName)
		
		# GSInstance.fullName
		self.assertString(instance.fullName)
		
		# GSInstance.customParameters
		instance.customParameters['trademark'] = 'ThisFont is a trademark by MyFoundry.com'
		self.assertGreaterEqual(len(instance.customParameters), 1)
		del(instance.customParameters['trademark'])
		
		# GSInstance.instanceInterpolations
		self.assertIsInstance(dict(instance.instanceInterpolations), dict)
		
		# GSInstance.manualInterpolation
		self.assertBool(instance.manualInterpolation)
		
		# GSInstance.interpolatedFont
		self.assertIsInstance(instance.interpolatedFont, type(Glyphs.font))
		
		
		## Methods
		
		# GSInstance.generate()
		self.assertEqual(instance.generate(FontPath = os.path.join(os.path.dirname(__file__), 'Glyphs Unit Test Sans.otf')), True)


	def test_GSGlyph(self):
		
		glyph = GlyphsApp.GSGlyph()
		glyph.name = 'test'
		Glyphs.font.glyphs.append(glyph)
		self.assertIsNotNone(glyph.__repr__())
		
		# GSGlyph.parent
		self.assertEqual(glyph.parent, Glyphs.font)
		
		# GSGlyph.layers
		glyph.layers = Glyphs.font.glyphs['a'].layers
		
		# GSGlyph.name
		self.assertUnicode(glyph.name)
		
		# GSGlyph.unicode
		self.assertUnicode(glyph.unicode)
		
		# GSGlyph.string
		if glyph.unicode:
			self.assertIsInstance(glyph.string, unicode)
		
		# GSGlyph.id
		self.assertIsInstance(glyph.id, str)
		
		# GSGlyph.category
		assert type(glyph.category) == unicode or type(glyph.category) == type(None)
		
		# GSGlyph.storeCategory
		self.assertBool(glyph.storeCategory)
		
		# GSGlyph.subCategory
		assert type(glyph.subCategory) == unicode or type(glyph.subCategory) == type(None)
		
		# GSGlyph.storeSubCategory
		self.assertBool(glyph.storeSubCategory)
		
		# GSGlyph.script
		self.assertTrue(type(glyph.category) == unicode or type(glyph.category) == type(None))
		
		# GSGlyph.storeScript
		self.assertBool(glyph.storeScript)
		
		# GSGlyph.productionName
		self.assertTrue(type(glyph.productionName) == unicode or type(glyph.productionName) == type(None))
		
		# GSGlyph.storeProductionName
		self.assertBool(glyph.storeProductionName)
		
		# GSGlyph.glyphInfo
		self.assertTrue(glyph.glyphInfo != None or glyph.glyphInfo == None)
		
		# GSGlyph.leftKerningGroup
		self.assertUnicode(glyph.leftKerningGroup)
		
		# GSGlyph.rightKerningGroup
		self.assertUnicode(glyph.rightKerningGroup)
		
		# GSGlyph.leftMetricsKey
		self.assertUnicode(glyph.leftMetricsKey)
		
		# GSGlyph.rightMetricsKey
		self.assertUnicode(glyph.rightMetricsKey)
		
		# GSGlyph.widthMetricsKey
		self.assertUnicode(glyph.widthMetricsKey)
		
		# GSGlyph.export
		self.assertBool(glyph.export)
		
		# GSGlyph.color
		self.assertInteger(glyph.color)
		
		# GSGlyph.colorObject
		glyph.color = 1
		self.assertIsInstance(glyph.colorObject, NSColor)
		
		# GSGlyph.note
		self.assertUnicode(glyph.note)
		
		# GSGlyph.selected
		self.assertBool(glyph.selected)
		
		# GSGlyph.mastersCompatible
		self.assertIsInstance(glyph.mastersCompatible, bool)
		
		# GSGlyph.userData
		self.assertIsNotNone(glyph.userData)
		if (len(glyph.userData) > 0):
			self.assertDict(glyph.userData)
		
		# GSGlyph.smartComponentAxes
		self.assertIsInstance(list(glyph.smartComponentAxes), list)
		
		# GSGlyph.lastChange
		self.assertInteger(glyph.lastChange, readOnly = True)
		
		
		## Methods
		glyph.beginUndo()
		glyph.endUndo()
		glyph.updateGlyphInfo()

		
		# Delete glyph
		del Glyphs.font.glyphs['test']
	

	def test_GSLayer(self):

		
		layer = Glyphs.font.glyphs['a'].layers[0]
		self.assertIsNotNone(layer.__repr__())

		# GSLayer.parent
		self.assertEqual(layer.parent, Glyphs.font.glyphs['a'])
		
		# GSLayer.name
		self.assertUnicode(layer.name)

		# GSLayer.associatedMasterId
		self.assertEqual(layer.associatedMasterId, Glyphs.font.masters[0].id)

		# GSLayer.layerId
		self.assertEqual(layer.layerId, Glyphs.font.masters[0].id)
		
		# GSLayer.color
		self.assertString(layer.color)
		
		# GSLayer.colorObject
		layer.color = 1
		self.assertIsInstance(glyph.colorObject, NSColor)
		
		# GSLayer.components
		layer = Glyphs.font.glyphs['adieresis'].layers[0]
		self.assertEqual(len(layer.components), 2)
		layer.components = []
		self.assertEqual(len(layer.components), 0)
		layer.components.append(GSComponent('a'))
		self.assertIsNotNone(layer.components[0].__repr__())
		self.assertEqual(len(layer.components), 1)
		layer.components.append(GSComponent('dieresis'))
		self.assertEqual(len(layer.components), 2)
		layer.components = [GSComponent('a'), GSComponent('dieresis')]
		self.assertEqual(len(layer.components), 2)

		# GSLayer.guides
		self.assertIsInstance(list(layer.guides), list)
		layer.guides = []
		self.assertEqual(len(layer.guides), 0)
		newGuide = GSGuideLine()
		newGuide.position = NSPoint(100, 100)
		newGuide.angle = -10.0
		layer.guides.append(newGuide)
		self.assertIsNotNone(layer.guides[0].__repr__())
		self.assertEqual(len(layer.guides), 1)
		del layer.guides[0]
		self.assertEqual(len(layer.guides), 0)

		# GSLayer.annotations
		layer.annotations = []
		self.assertEqual(len(layer.annotations), 0)
		newAnnotation = GSAnnotation()
		newAnnotation.type = TEXT
		newAnnotation.text = 'Fuck, this curve is ugly!'
		layer.annotations.append(newAnnotation)
		self.assertIsNotNone(layer.annotations[0].__repr__())
		self.assertEqual(len(layer.annotations), 1)
		del layer.annotations[0]
		self.assertEqual(len(layer.annotations), 0)

		# GSLayer.hints
		layer = Glyphs.font.glyphs['a'].layers[0]
		layer.hints = []
		self.assertEqual(len(layer.hints), 0)
		newHint = GSHint()
		newHint.originNode = layer.paths[0].nodes[0]
		newHint.targetNode = layer.paths[0].nodes[1]
		newHint.type = STEM
		layer.hints.append(newHint)
		self.assertIsNotNone(layer.hints[0].__repr__())
		self.assertEqual(len(layer.hints), 1)
		del layer.hints[0]
		self.assertEqual(len(layer.hints), 0)

		# GSLayer.anchors
		if layer.anchors['top']:
			oldPosition = layer.anchors['top'].position
		else:
			oldPosition = None
		layer.anchors['top'] = GSAnchor()
		self.assertGreaterEqual(len(layer.anchors), 1)
		self.assertIsNotNone(layer.anchors['top'].__repr__())
		layer.anchors['top'].position = NSPoint(100, 100)
		del layer.anchors['top']
		layer.anchors['top'] = GSAnchor()
		layer.anchors['top'].position = oldPosition


sys.argv = ["GlyphsAppTests"]

if __name__ == '__main__':
	unittest.main(exit=False)
