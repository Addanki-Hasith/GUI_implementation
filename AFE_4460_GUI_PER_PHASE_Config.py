class phase_type(QtGui.QWidget):
	def __init__(self):
		super(phase_type,self).__init__()
		
# 		Required Widgets
		self.title			 			= QtGui.QLabel('PHASE TYPE')
		self.val1 						= QtGui.QRadioButton('Explicitly defined AMB')
		self.val2 			 			= QtGui.QRadioButton('LED without Auto AMBs')
		self.val3			 			= QtGui.QRadioButton('LED with Auto AMBs')	
		self.val3_op1		 			= QtGui.QRadioButton('None')
		self.val3_op2		 			= QtGui.QRadioButton('Pre AMB')
		self.val3_op3		 			= QtGui.QRadioButton('Pre and Post AMB')

# 		Setting ToolTips
		settingToolTip(		self.title, 		"Configuration of PHASE TYPE")
		settingToolTip(		self.val1, 			"Setting Explicity defined Ambient Phase")
		settingToolTip(		self.val2, 			"Setting LED phase without any Auto Ambients")
		settingToolTip(		self.val3, 			"Setting LED Phase with Auto Ambients")
		settingToolTip(		self.val3_op1,		"Setting LED Phase with No Auto Ambients")
		settingToolTip(		self.val3_op2,		"Setting LED Phase with only PRE Ambient phase")
		settingToolTip(		self.val3_op3,		"Setting LED Phase with both PRE and POST Ambient phases")

# 		Styling of each widget
		titles_styling(					self.title)
		
		normal_radioButton_styling(		self.val1)
		normal_radioButton_styling(		self.val2)
		normal_radioButton_styling( 	self.val3)
		small_radioButton_styling(		self.val3_op1)
		small_radioButton_styling(		self.val3_op2)
		small_radioButton_styling(		self.val3_op3)

# 		Resizing 
		resizingPolicy(		self.title)
		resizingPolicy(		self.val1)
		resizingPolicy(		self.val2)
		resizingPolicy( 	self.val3)
		resizingPolicy(		self.val3_op1)
		resizingPolicy(		self.val3_op2)
		resizingPolicy(		self.val3_op3)

# 		Grouping Radio Buttons
		self.main_grp		 			= QtGui.QButtonGroup()
		self.sub_grp		 			= QtGui.QButtonGroup()
		self.main_grp.addButton(	self.val1)
		self.main_grp.addButton(	self.val2)
		self.main_grp.addButton(	self.val3)
		
		self.sub_grp.addButton(		self.val3_op1)
		self.sub_grp.addButton(		self.val3_op2)
		self.sub_grp.addButton(		self.val3_op3)

# 		Layouts and Arrangement		
		self.MainLay 				= QtGui.QGridLayout()
		self.MainLay.addWidget(		self.title,				0,0,1,3)
		self.MainLay.addWidget(		self.val1,				1,0,1,5)
		self.MainLay.addWidget(		self.val2,				2,0,1,5)
		self.MainLay.addWidget(		self.val3,				3,0,1,5)
		self.MainLay.addWidget(		self.val3_op1,			4,1,1,2)
		self.MainLay.addWidget(		self.val3_op2,			5,1,1,3)
		self.MainLay.addWidget(		self.val3_op3,			6,1,1,3)
			
# 		setting the widget layout
		self.setLayout(						self.MainLay)
		
# 		Widget Background Styling
		Widget_Background(self)
		

class transmitter_config(QtGui.QWidget):
	def __init__(self):
		super(transmitter_config,self).__init__()

# 		Required Widgets
		self.title 				= QtGui.QLabel('TRANSMITTER')
		self.LedOn 				= QtGui.QLabel('LED ON Time')
		self.FilterSet 			= QtGui.QLabel('Filter Set Selected')
		self.DRV_TXP 			= QtGui.QLabel('DRV_TXP')	
		self.DRV_TXN1 			= QtGui.QLabel('DRV_TXN1')
		self.DRV_TXN2 			= QtGui.QLabel('DRV_TXN2')	
		self.ILED_DRV1 			= QtGui.QLabel('ILED_DRV1 (mA)')
		self.ILED_DRV2 			= QtGui.QLabel('ILED_DRV2 (mA)')
		
# 		Setting ToolTips
		settingToolTip(		self.title,			"Per Phase Configuration of Transmitter")
		settingToolTip(		self.LedOn,			"Select required LED On Time")
		settingToolTip(		self.FilterSet,		"This Filter Set is chosen automatically bases on selected LED ON TIME")
		settingToolTip(		self.DRV_TXP,		"Select the required TXP for the DRIVER")
		settingToolTip(		self.DRV_TXN1,		"Select the required TXN for DRIVER1")
		settingToolTip(		self.DRV_TXN2,		"Select the required TXn for DRIVER2")
		settingToolTip(		self.ILED_DRV1,		"Configuration of LED current in DRIVER1")
		settingToolTip(		self.ILED_DRV2,		"Configuration of LED current in DRIVER2")
		
# 		Defining comboboxes required and its values
		self.LedOnCombo 		= QtGui.QComboBox()
		
		self.DRV_TXPCombo 		= QtGui.QComboBox()
		self.DRV_TXPCombo.addItems(['None','TXP1','TXP2','TXP3','TXP4'])
		
		self.DRV_TXN1Combo 		= QtGui.QComboBox()
		self.DRV_TXN1Combo.addItems(['None','TXN1','TXN2','TXN3','TXN4','TXN5','TXN6','TXN7','TXN8'])
		
		self.DRV_TXN2Combo		= QtGui.QComboBox()
		self.DRV_TXN2Combo.addItems(['None','TXN1','TXN2','TXN3','TXN4','TXN5','TXN6','TXN7','TXN8'])
		
# 		Defining lineEdits required
		self.userval1 = QtGui.QLineEdit()
		self.userval1.setPlaceholderText('in mA')
		
		self.userval2 = QtGui.QLineEdit()
		self.userval2.setPlaceholderText('in mA')
		
# 		Styling
		titles_styling(			self.title)
		Boxedlabel_styling(		self.LedOn)
		
		AutoAssignedLabel(		self.FilterSet)
		
		Boxedlabel_styling(		self.DRV_TXP)
		Boxedlabel_styling(		self.DRV_TXN1)
		Boxedlabel_styling(		self.DRV_TXN2)
		Boxedlabel_styling(		self.ILED_DRV1)
		Boxedlabel_styling(		self.ILED_DRV2)
		
		lineEditStyling(		self.userval1)
		lineEditStyling(		self.userval2)
		
		TextAlignCenter(		self.LedOn)
		TextAlignCenter(		self.FilterSet)
		TextAlignCenter(		self.DRV_TXP)
		TextAlignCenter(		self.DRV_TXN1)
		TextAlignCenter(		self.DRV_TXN2)
		TextAlignCenter(		self.ILED_DRV1)
		TextAlignCenter(		self.ILED_DRV2)
		
		TextAlignCenter(		self.userval1)
		TextAlignCenter(		self.userval2)
		
		
# 		Resizing
		resizingPolicy(		self.title)
		resizingPolicy(		self.LedOn)
		resizingPolicy(		self.FilterSet)
		resizingPolicy(		self.DRV_TXP)
		resizingPolicy(		self.DRV_TXN1)
		resizingPolicy(		self.DRV_TXN2)
		
		lineEditPolicy(		self.ILED_DRV1)
		lineEditPolicy(		self.ILED_DRV2)
		
# 		Layouts and Arrangement

		self.LedOnForm 					= QtGui.QHBoxLayout()
		self.LedOnForm.addWidget(		self.LedOn,			4)
		self.LedOnForm.addWidget(		self.LedOnCombo,	1)
		
		self.DRV_TXPForm 				= QtGui.QHBoxLayout()
		self.DRV_TXPForm.addWidget(		self.DRV_TXP,		3)
		self.DRV_TXPForm.addWidget(		self.DRV_TXPCombo,	1)
		
		self.DRV_TXN1Form 				= QtGui.QHBoxLayout()
		self.DRV_TXN1Form.addWidget(	self.DRV_TXN1,		3)
		self.DRV_TXN1Form.addWidget(	self.DRV_TXN1Combo,	1)
		
		self.DRV_TXN2Form 				= QtGui.QHBoxLayout()
		self.DRV_TXN2Form.addWidget(	self.DRV_TXN2,		3)
		self.DRV_TXN2Form.addWidget(	self.DRV_TXN2Combo,	1)
	
		self.ILED_DRV1Form				= QtGui.QHBoxLayout()
		self.ILED_DRV1Form.addWidget(	self.ILED_DRV1,		3)
		self.ILED_DRV1Form.addWidget(	self.userval1,		1)

		self.ILED_DRV2Form 				= QtGui.QHBoxLayout()
		self.ILED_DRV2Form.addWidget(	self.ILED_DRV2,		3)
		self.ILED_DRV2Form.addWidget(	self.userval2,		1)
		
		self.transmitter_config_lay 				= QtGui.QGridLayout()
		self.transmitter_config_lay.addWidget(		self.title,				0,0,1,3)
		self.transmitter_config_lay.addLayout(		self.LedOnForm,			1,0,1,5)
		self.transmitter_config_lay.addWidget(		self.FilterSet,			2,0,1,5)
		self.transmitter_config_lay.addLayout(		self.DRV_TXPForm,		3,0,1,5)
		self.transmitter_config_lay.addLayout(		self.DRV_TXN1Form,		4,0,1,5)
		self.transmitter_config_lay.addLayout(		self.DRV_TXN2Form,		5,0,1,5)
		self.transmitter_config_lay.addLayout(		self.ILED_DRV1Form,		6,0,1,5)
		self.transmitter_config_lay.addLayout(		self.ILED_DRV2Form,		7,0,1,5)
		
# 		setting the widget layout
		self.setLayout(self.transmitter_config_lay)
		
# 		Widget Background Styling
		Widget_Background(self)
		
# 		internal configurations
		
		self.LED_ON_LabelsSet = ['None','None','None']
		
		self.LedOnCombo.addItems(self.LED_ON_LabelsSet)
		self.LedOnCombo.currentIndexChanged.connect(self.LED_Filter_config)
		
		self.DRV_TXPCombo.currentIndexChanged.connect(self.drv_txp_config)
		self.DRV_TXN1Combo.currentIndexChanged.connect(self.drv1_txn_config)
		self.DRV_TXN2Combo.currentIndexChanged.connect(self.drv2_txn_config)
		
		
			
		self.onlyDouble = QtGui.QDoubleValidator()
		self.userval1.setValidator(self.onlyDouble)
		self.onlyDouble.setNotation(QtGui.QDoubleValidator.StandardNotation)
		
		self.onlyDouble2 = QtGui.QDoubleValidator()
		self.userval2.setValidator(self.onlyDouble)
		self.onlyDouble2.setNotation(QtGui.QDoubleValidator.StandardNotation)
		
		
		self.userval1.editingFinished.connect(self.iled_drv1_config)
		self.userval2.editingFinished.connect(self.iled_drv2_config)
		
		self.DRV_TXPCombo.setEnabled(False)
		self.DRV_TXN1Combo.setEnabled(False)
		self.DRV_TXN2Combo.setEnabled(False)
		
	def LED_ON1_Time_label(self,i):
		self.LED_ON_LabelsSet[1] = LED_ON_TImings_Labels[i]
		self.LedOnCombo.clear()
		self.LedOnCombo.addItems(self.LED_ON_LabelsSet)
		
	def LED_ON2_Time_label(self,i):
		self.LED_ON_LabelsSet[2] = LED_ON_TImings_Labels[i]
		self.LedOnCombo.clear()
		self.LedOnCombo.addItems(self.LED_ON_LabelsSet)
		
	def LED_Filter_config(self,i):
		if i == 0:
			logWindow_wid.settingLogText('Select correct option')
			
		else:
			if i == 1:
				AFE_config_LEDOnTime_width(1,LED1_ON_TIME_GLOBAL[0],0)
				self.FilterSet.setText('Filter Set-1 is selected')
				
			elif i == 2:
				AFE_config_LEDOnTime_width(1,LED2_ON_TIME_GLOBAL[0],1)
				self.FilterSet.setText('Filter Set-2 is selected')
				
			
			self.DRV_TXPCombo.setEnabled(True)
	def drv_txp_txn_AMB_reset(self):
		self.DRV_TXPCombo.setCurrentIndex(0)
		self.DRV_TXN1Combo.setCurrentIndex(0)
		self.DRV_TXN2Combo.setCurrentIndex(0)
		self.userval1.clear()
		self.userval2.clear()
		
		self.DRV_TXPCombo.setEnabled(False)
		self.DRV_TXN1Combo.setEnabled(False)		
		self.DRV_TXN2Combo.setEnabled(False)
		self.userval1.setEnabled(False)
		self.userval2.setEnabled(False)
		
		AFE_config_Drv_TXP(1,AMB_PH_TXP)
		AFE_config_Drv1_TXN(1,AMB_PH_TXN)
		AFE_config_Drv2_TXN(1,AMB_PH_TXP)
	
	def drv_txp_txn_LED_enable(self):
		self.DRV_TXPCombo.setCurrentIndex(0)
		self.DRV_TXN1Combo.setCurrentIndex(0)
		self.DRV_TXN2Combo.setCurrentIndex(0)
		self.userval1.clear()
		self.userval2.clear()
		
		self.DRV_TXPCombo.setEnabled(True)
# 		self.DRV_TXN1Combo.setEnabled(True)		
# 		self.DRV_TXN2Combo.setEnabled(True)
# 		self.userval1.setEnabled(True)
# 		self.userval2.setEnabled(True)
	
	def drv_txp_config(self,i):
		if i == 0:
			logWindow_wid.settingLogText('Select correct option')
		else:
			val = 0
			if i == 1:
				val = LED_PH_TXP1
			elif i == 2:
				val = LED_PH_TXP2
			elif i == 3:
				val = LED_PH_TXP3
			elif i == 4:
				val = LED_PH_TXP4
			
			AFE_config_Drv_TXP(	1, val)
			
			logWindow_wid.settingLogText('TXP Driver is configured')
			
			self.DRV_TXN1Combo.setEnabled(True)
			
	def drv1_txn_config(self,i):
		if i == 0:
			logWindow_wid.settingLogText('Select correct option')
		else:
			val = 0 
			if i == 1:
				val = LED_PH_TXN1
			elif i == 2:
				val = LED_PH_TXN2
			elif i == 3:
				val = LED_PH_TXN3
			elif i == 4:
				val = LED_PH_TXN4
			elif i == 5:
				val = LED_PH_TXN5
			elif i == 6:
				val =LED_PH_TXN6
			elif i == 7:
				val = LED_PH_TXN7
			elif i == 8:
				val = LED_PH_TXN8
			
			AFE_config_Drv1_TXN( 1, val)
			logWindow_wid.settingLogText('TXN Driver1 is configured')
			
			self.DRV_TXN2Combo.setEnabled(True)
	
	def drv2_txn_config(self,i):
		if i == 0:
			logWindow_wid.settingLogText('Select correct option')
		else:
			val = 0 
			if i == 1:
				val = LED_PH_TXN1
			elif i == 2:
				val = LED_PH_TXN2
			elif i == 3:
				val = LED_PH_TXN3
			elif i == 4:
				val = LED_PH_TXN4
			elif i == 5:
				val = LED_PH_TXN5
			elif i == 6:
				val =LED_PH_TXN6
			elif i == 7:
				val = LED_PH_TXN7
			elif i == 8:
				val = LED_PH_TXN8
				
			AFE_config_Drv2_TXN( 1, val)
			logWindow_wid.settingLogText('TXN Driver2 is configured')
			
			
			if FS_LED_CURRENT_global[0]:
				self.userval1.setToolTip('Enter values between 0mA and '+str(FS_LED_CURRENT_global[0])+'A')
				self.userval2.setToolTip('Enter values between 0mA and '+str(FS_LED_CURRENT_global[0])+'A')
				self.onlyDouble.setRange(0,FS_LED_CURRENT_global[0],decimals = 3)
				self.onlyDouble2.setRange(0,FS_LED_CURRENT_global[0],decimals = 3)	
				self.userval1.setEnabled(True)
				self.userval2.setEnabled(True)
				
			else:
				self.userval1.setToolTip('Configure Full Scale LED Current')
				self.userval2.setToolTip('Configure Full Scale LED Current')
			
			
	def iled_drv1_config(self):
		self.userval1.clearFocus()
		
		val = float(str(self.userval1.text()))
		AFE_config_ILED_DRV1( 1, val)
		
	def iled_drv2_config(self):
		self.userval2.clearFocus()
		
		val = float(str(self.userval2.text()))
		AFE_config_ILED_DRV2( 1, val)
		
		
class tia_config(QtGui.QWidget):
	def __init__(self):
		super(tia_config,self).__init__()

# 		Required Widgets		
		self.title 						=  QtGui.QLabel('TIA n')
		self.subTitle_PD 				= QtGui.QLabel('PDs connected to TIA : ')
		self.PD1_checkbox 				= QtGui.QCheckBox('PD1')
		self.PD2_checkbox 				= QtGui.QCheckBox('PD2')
		self.PD3_checkbox 				= QtGui.QCheckBox('PD3')
		self.PD4_checkbox 				= QtGui.QCheckBox('PD4')
		self.RF_label 					= QtGui.QLabel('RF')		
		self.CF_ValLabel 				= QtGui.QLabel('Assigned CF')
		
		ioffdac_str 					= 'IOFFDAC_LED (' + unichr(int('b5',16))+'A)'
		self.IOFFDAC_LEDLabel 			= QtGui.QLabel(ioffdac_str)
		
		self.EnableDC 					= QtGui.QLabel('Enable LED DC\n Cancellation')
		
		self.EnableDCYes 				= QtGui.QRadioButton('Yes')
		self.EnableDCNo					= QtGui.QRadioButton('No')
		
# 		Defining comboboxes, lineEdits required and its values
		self.RF_Combo 					= QtGui.QComboBox()
		self.RF_Combo.addItems(			['3.7 KOhm','5 KOhm','10 KOhm','25 KOhm','33.3 KOhm','50 KOhm','71.5 KOhm', 														'100KOhm','142 KOhm','166 KOhm','200 KOhm','250 KOhm','500 KOhm','1 MOhm'])
				
		place_holderText 				= 'in ' + unichr(int('b5',16)) +'A'
		self.IOFFDAC_userval			= QtGui.QLineEdit()
		self.IOFFDAC_userval.setPlaceholderText(place_holderText)	

# 		Setting ToolTips
		settingToolTip(		self.title,				"Configuration of TIA")
		settingToolTip(		self.subTitle_PD,		"Select the PDs to be connected")
		settingToolTip(		self.RF_label,			"Select the required FeedBack Resistance of TIA")
		settingToolTip(		self.CF_ValLabel,		"Automatically assigned FeedBack Capacitance of TIA")
		settingToolTip(		self.IOFFDAC_LEDLabel,	"Configuration of OFFSET LED Current")
		settingToolTip(		self.EnableDC,			"Choose yes if LED DC Cancellation to be enabled")
		
# 		Styling
		titles_styling(					self.title)
		UnderlineLabel_styling(			self.subTitle_PD)
		Boxedlabel_styling(				self.RF_label)

		AutoAssignedLabel(				self.CF_ValLabel)
		
		Boxedlabel_styling(				self.IOFFDAC_LEDLabel)
		Boxedlabel_styling(				self.EnableDC)
		normal_radioButton_styling(		self.EnableDCYes)
		normal_radioButton_styling(		self.EnableDCNo)
		
		lineEditStyling(				self.IOFFDAC_userval)
		
		TextAlignCenter(		self.subTitle_PD)
		TextAlignCenter(		self.RF_label)
		TextAlignCenter(		self.CF_ValLabel)
		TextAlignCenter(		self.IOFFDAC_LEDLabel)
		TextAlignCenter(		self.IOFFDAC_userval)

# 		Resizing
		resizingPolicy(				self.title)
		resizingPolicy(				self.subTitle_PD)
		resizingPolicy(				self.PD1_checkbox)
		resizingPolicy(				self.PD2_checkbox)
		resizingPolicy(				self.PD3_checkbox)
		resizingPolicy(				self.PD4_checkbox)
		resizingPolicy(				self.RF_label)
		resizingPolicy(				self.RF_Combo)
		resizingPolicy(				self.CF_ValLabel)
		
		lineEditPolicy(				self.IOFFDAC_LEDLabel)
		lineEditPolicy(				self.IOFFDAC_userval)
		
		resizingPolicy(				self.EnableDC)
		resizingPolicy(				self.EnableDCYes)
		resizingPolicy(				self.EnableDCNo)
	
		
		self.RF_Form 						= QtGui.QHBoxLayout()
		self.RF_Form.addWidget(				self.RF_label,				3)
		self.RF_Form.addWidget(				self.RF_Combo,				1)
	
		self.IOFFDAC_Form 					= QtGui.QHBoxLayout()
		self.IOFFDAC_Form.addWidget(		self.IOFFDAC_LEDLabel,		3)
		self.IOFFDAC_Form.addWidget(		self.IOFFDAC_userval,		1)
		
		self.EnableDCbool 					= QtGui.QVBoxLayout()
		self.EnableDCbool.addWidget(		self.EnableDCYes)
		self.EnableDCbool.addWidget(		self.EnableDCNo)
		
		self.EnableDC_Form 					= QtGui.QHBoxLayout()
		self.EnableDC_Form.addWidget(		self.EnableDC)
		self.EnableDC_Form.addLayout(		self.EnableDCbool)
		
		self.tia_config_lay 				= QtGui.QGridLayout()
		self.tia_config_lay.addWidget(		self.title,					0,0,1,1)
		self.tia_config_lay.addWidget(		self.subTitle_PD,			1,0,1,4)
		self.tia_config_lay.addWidget(		self.PD1_checkbox,			2,0,1,2)
		self.tia_config_lay.addWidget(		self.PD2_checkbox,			2,2,1,2)
		self.tia_config_lay.addWidget(		self.PD3_checkbox,			3,0,1,2)
		self.tia_config_lay.addWidget(		self.PD4_checkbox,			3,2,1,2)
		self.tia_config_lay.addLayout(		self.RF_Form,				4,0,1,4)
		self.tia_config_lay.addWidget(		self.CF_ValLabel,			5,0,1,4)
		self.tia_config_lay.addLayout(		self.IOFFDAC_Form,			6,0,1,4)
		self.tia_config_lay.addLayout(		self.EnableDC_Form,			7,0,1,4)
		
# 		setting the widget layout
		self.setLayout(self.tia_config_lay)
		
# 		Widget Background Styling
		Widget_Background(self)
		
		
class receiver_config(QtGui.QWidget):
	def __init__(self):
		super(receiver_config,self).__init__()

# 		Required Widgets		
		self.title 					= QtGui.QLabel('RECEIVER')
		self.NoofTIAs 				= QtGui.QLabel('No. of TIAs')
		self.NUMAV 					= QtGui.QLabel('NUMAV')
		self.SchemeforAMB 			= QtGui.QLabel('Scheme for AMB Cancellation')
		self.FIFOCtrl 				= QtGui.QLabel('FIFO DATA CTRL')
		self.MaskingFactor 			= QtGui.QLabel('Masking Factor')
		self.EnableDRE 				= QtGui.QLabel('Enable DRE')
		self.DecimationFactor 		= QtGui.QLabel('Decimation Factor')

# 		Defining booleans,comboboxes required and its values
		self.NoofTIAsCombo 			= QtGui.QComboBox()
		
		self.NUMAVCombo 			= QtGui.QComboBox()
		self.NUMAVCombo.addItems(['1','2','3','4','8'])

		self.SchemeforAMBCombo 		= QtGui.QComboBox()
		self.SchemeforAMBCombo.addItems(['AACM OFF','Estimate and Cancel AACM','Cancel AACM without Estimation'])
		
		self.FIFOCtrlCombo 			= QtGui.QComboBox()
		self.FIFOCtrlCombo.addItems(['None'])
		
		self.MaskingFactorCombo 	= QtGui.QComboBox()
		self.MaskingFactorCombo.addItems(['None'])
		
		self.EnableDRE_yes 			= QtGui.QRadioButton('YES')
		self.EnableDRE_no 			= QtGui.QRadioButton('NO')
		
		self.DecimationFactorCombo 	= QtGui.QComboBox()
		self.DecimationFactorCombo.addItems(['NO Decimation','Decimation by 2','Decimation by 4','Decimation by 8','Decimation by 16','Decimation by 32'])
		
# 		Setting ToolTips
		settingToolTip(		self.title,				"Per Phase Configuration of Receiver")
		settingToolTip(		self.NoofTIAs,			"Select the Number of Required in this phase")
		settingToolTip(		self.NUMAV,				"Select the Number of ADC Averages required")
		settingToolTip(		self.SchemeforAMB,		"Select the required Ambient Cancellation scheme")
		settingToolTip(		self.EnableDRE,			"Choose yes if DRE (Dynamic RANGE Extension) mode to be enabled")
		settingToolTip(		self.FIFOCtrl,			"Select the required FIFO Data Control")
		settingToolTip(		self.MaskingFactor,		"Select the required Masking Factor")
		settingToolTip(		self.DecimationFactor,	"Select the Output Decimation Factor")

# 		Styling
		titles_styling(					self.title)
		Boxedlabel_styling(				self.NoofTIAs)
		Boxedlabel_styling(				self.NUMAV)
		Boxedlabel_styling(				self.SchemeforAMB)
		Boxedlabel_styling(				self.EnableDRE)
		Boxedlabel_styling(				self.FIFOCtrl)
		Boxedlabel_styling(				self.MaskingFactor)
		Boxedlabel_styling(				self.DecimationFactor)
		
		normal_radioButton_styling(		self.EnableDRE_yes)
		normal_radioButton_styling(		self.EnableDRE_no)
		
		self.title.setAlignment(		QtCore.Qt.AlignLeft)
		TextAlignCenter(				self.NoofTIAs)
		TextAlignCenter(				self.NUMAV)
		TextAlignCenter(				self.SchemeforAMB)
		TextAlignCenter(				self.EnableDRE)
		TextAlignCenter(				self.FIFOCtrl)
		TextAlignCenter(				self.MaskingFactor)
		TextAlignCenter(				self.DecimationFactor)
		
# 		Resizing
		resizingPolicy(		self.title)
		resizingPolicy(		self.NoofTIAs)
		resizingPolicy(		self.NUMAV)
		resizingPolicy(		self.SchemeforAMB)
		resizingPolicy(		self.EnableDRE)
		resizingPolicy(		self.FIFOCtrl)
		resizingPolicy(		self.MaskingFactor)
		resizingPolicy(		self.EnableDRE)
		
		resizingPolicy(		self.NoofTIAsCombo)
		
		resizingPolicy(		self.NUMAVCombo)
		resizingPolicy(		self.SchemeforAMBCombo)
		resizingPolicy(		self.EnableDRE_yes)
		resizingPolicy(		self.EnableDRE_no)
		resizingPolicy(		self.FIFOCtrlCombo)
		resizingPolicy(		self.MaskingFactorCombo)
		resizingPolicy(		self.DecimationFactorCombo)
		
# 		Layouts and Arrangement
		self.NoofTIAs_lay 						= QtGui.QHBoxLayout()
		self.NoofTIAs_lay.addWidget(			self.NoofTIAs,				3)
		self.NoofTIAs_lay.addWidget(			self.NoofTIAsCombo,			1)
		
		self.NUMAV_lay 							= QtGui.QHBoxLayout()
		self.NUMAV_lay.addWidget(				self.NUMAV,					3)
		self.NUMAV_lay.addWidget(				self.NUMAVCombo,			1)
		
		self.SchemeforAMB_lay 					= QtGui.QHBoxLayout()
		self.SchemeforAMB_lay.addWidget(		self.SchemeforAMB,			4)
		self.SchemeforAMB_lay.addWidget(		self.SchemeforAMBCombo,		1)
		
		self.EnableDRE_bool 					= QtGui.QFormLayout()
		self.EnableDRE_bool.addRow(				self.EnableDRE_yes,self.EnableDRE_no)
		
		self.EnableDRE_bool_wid 				= QtGui.QWidget()
		self.EnableDRE_bool_wid.setLayout(		self.EnableDRE_bool)
		
		self.FIFOCtrlForm 						= QtGui.QHBoxLayout()
		self.FIFOCtrlForm.addWidget(			self.FIFOCtrl,				3)
		self.FIFOCtrlForm.addWidget(			self.FIFOCtrlCombo,			4)
		
		self.MaskingFactorForm 					= QtGui.QHBoxLayout()
		self.MaskingFactorForm.addWidget(		self.MaskingFactor,			3)
		self.MaskingFactorForm.addWidget(		self.MaskingFactorCombo,	3)
		
		self.DecimationFactorForm 				= QtGui.QHBoxLayout()
		self.DecimationFactorForm.addWidget(	self.DecimationFactor,		4)
		self.DecimationFactorForm.addWidget(	self.DecimationFactorCombo,	3)
		
		self.MainLay 				= QtGui.QGridLayout()
		self.MainLay.addWidget(		self.title,					0,0,1,4)
		self.MainLay.addLayout(		self.NoofTIAs_lay,			1,0,1,4)
		self.MainLay.addLayout(		self.NUMAV_lay,				2,0,1,4)
		self.MainLay.addLayout(		self.SchemeforAMB_lay,		3,0,1,9)
		self.MainLay.addWidget(		self.EnableDRE,				3,11,1,2)
		self.MainLay.addWidget(		self.EnableDRE_bool_wid,	3,13,1,2)
		self.MainLay.addLayout(		self.FIFOCtrlForm,			4,0,1,4)
		self.MainLay.addLayout(		self.MaskingFactorForm,		4,5,1,5)
		self.MainLay.addLayout(		self.DecimationFactorForm,	4,11,1,4)		

# 		setting the widget layout
		self.setLayout(self.MainLay)

# 		Widget Background Styling
		Widget_Background(self)
		
# 		internal configurations
		self.NoofTIAsCombo.addItem('None')
	def config_noOfTIAs(self,i):
		self.NoofTIAsCombo.clear()
		self.NoofTIAsCombo.addItem('None')
		for j in range(i):
			self.NoofTIAsCombo.addItem(str(j+1))

								
class Individual_config_layout(QtGui.QWidget):
	def __init__(self):
		super(Individual_config_layout,self).__init__()
		
		sub_lay 				= QtGui.QVBoxLayout()
		self.phaseType 			= phase_type()
		self.transmitter 		= transmitter_config()
		self.receiver 			= receiver_config()
		
		self.tia1 = tia_config()
		self.tia1.title.setText('TIA1')
		self.tia2 = tia_config()
		self.tia2.title.setText('TIA2')
		self.tia3 = tia_config()
		self.tia3.title.setText('TIA3')
		self.tia4 = tia_config()
		self.tia4.title.setText('TIA4')

		self.MainLay 				= QtGui.QGridLayout()
		self.MainLay.addWidget(		self.phaseType,			0,0,3,2)
		self.MainLay.addWidget(		self.transmitter,		3,0,4,2)
		self.MainLay.addWidget(		self.receiver,			0,2,3,7)
		self.MainLay.addWidget(		self.tia1,				3,2,3,1)
		self.MainLay.addWidget(		self.tia2,				3,4,3,1)
		self.MainLay.addWidget(		self.tia3,				3,6,3,1)		
		self.MainLay.addWidget(		self.tia4,				3,8,3,1)
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('white'))
		
		self.phaseType.val1.clicked.connect(self.transmitter.drv_txp_txn_AMB_reset)
		self.phaseType.val2.clicked.connect(self.transmitter.drv_txp_txn_LED_enable)
		self.phaseType.val3.clicked.connect(self.transmitter.drv_txp_txn_LED_enable)
# 		self.phaseType.val3_op1.clicked.connect(self.receiver....)
# 		self.phaseType.val3_op2.clicked.connect(self.receiver....)
# 		self.phaseType.val3_op3.clicked.connect(self.receiver....)
		
		
# 		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		self.setPalette(palette)
		self.setLayout(self.MainLay)
		
class Summary_config_layout(QtGui.QWidget):
	def __init__(self):
		super(Summary_config_layout,self).__init__()
		layout = QtGui.QHBoxLayout()
		layout.addWidget(Color('red'))
		
# 		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		self.setLayout(layout)

class control_layout2(QtGui.QWidget):
	def __init__(self):
		super(control_layout2,self).__init__()

# 		Required Widgets
		self.label1 		= QtGui.QLabel('Required \nNo. of Phases')
		self.userval1 		= QtGui.QComboBox()
		self.common_wid 	= QtGui.QRadioButton('Common')
		self.phN_arr = []
		for i in range(16):
			ph_str = 'PH' + str(i+1)
			self.phN_arr.append(QtGui.QRadioButton(ph_str))
		
		self.viewLabel 		= QtGui.QLabel('View')
		self.individual 	= QtGui.QRadioButton('Individual')
		self.summary 		= QtGui.QRadioButton('Summary')
		
# 		Setting ToolTips
		settingToolTip(		self.label1,			"Configuration of NUMBER of Phases required")
		settingToolTip(		self.common_wid,		"Setting all the common per phase configurations")
		for i in range(16):
			settingToolTip(	self.phN_arr[i],		"Configuration of parameters in this phase")
		settingToolTip(		self.viewLabel,			"Choose be individual configurations and summary of all the configurations")
		settingToolTip(		self.individual,		"Individual Per Phase Configurations view")
		settingToolTip(		self.summary,			"Summary of all the Per Phase Configurations made")
		
		
# 		Styling of each widget		
		titles_styling(					self.label1)
		normal_radioButton_styling(		self.common_wid)
		
		for i in range(16):
			small_radioButton_styling(	self.phN_arr[i])
			
		titles_styling(					self.viewLabel)
		normal_radioButton_styling(		self.individual)
		normal_radioButton_styling(		self.summary)
		
		TextAlignCenter(self.label1)
		self.viewLabel.setAlignment(QtCore.Qt.AlignRight)
		
# 		Resizing 		
		resizingPolicy(			self.label1)
		lineEditPolicy(			self.userval1)
		resizingPolicy(			self.common_wid)
		for i in range(16):
			resizingPolicy(		self.phN_arr[i])
		resizingPolicy(			self.viewLabel)
		resizingPolicy(			self.individual)
		resizingPolicy(			self.summary)
		
# 		Grouping Radio Buttons		
		self.common_ph_group 					= QtGui.QButtonGroup()
		self.common_ph_group.addButton(			self.common_wid)
		for i in range(16):
			self.common_ph_group.addButton(		self.phN_arr[i])
			
		self.view_group 						= QtGui.QButtonGroup()
		self.view_group.addButton(				self.individual)
		self.view_group.addButton(				self.summary)
		self.individual.setChecked(True)

# 		Layouts and Arrangement	
		self.labelForm 							= QtGui.QHBoxLayout()
		self.labelForm.addWidget(				self.label1,			3)
		self.labelForm.addWidget(				self.userval1,			1)
		
		self.MainLay 							= QtGui.QGridLayout()
		self.MainLay.addLayout(					self.labelForm,			0,0,2,2)
		self.MainLay.addWidget(					self.common_wid,		0,4,2,2)
		
		for i in range(8):
			self.MainLay.addWidget(				self.phN_arr[i],		0,i+6,1,1)
			self.MainLay.addWidget(				self.phN_arr[8+i],		1,i+6,1,1)
		
		self.MainLay.addWidget(					self.viewLabel,			0,16,2,1)
		self.MainLay.addWidget(					self.individual,		0,17,1,2)
		self.MainLay.addWidget(					self.summary,			1,17,1,2)
		
# 		setting the widget layout
		self.setLayout(self.MainLay)
# 		Widget Background Styling
		Widget_Background(self)
		
# 		internal configurations
		self.common_wid.setEnabled(False)
		self.opacity = []
		for i in range(16):
			self.opacity_effect 		= QtGui.QGraphicsOpacityEffect()
			self.opacity_effect.setOpacity(0.2)
			self.opacity.append(self.opacity_effect)
			self.phN_arr[i].setGraphicsEffect(self.opacity[i])
			self.phN_arr[i].setEnabled(False)
		
		
		self.userval1.addItem('None')
		for i in range(16):
			self.userval1.addItem(str(i+1))
		self.userval1.currentIndexChanged.connect(self.No_OF_TIAs_PPM)
				
		
	def No_OF_TIAs_PPM(self,i):
		if i == 0:
			logWindow_wid.settingLogText("Choose correct option")
		else:
			AFE_config_numOfPhases(i)
			for j in range(16):
				if j<i:
					self.opacity[j].setEnabled(False)
				else:
					self.opacity[j].setEnabled(True)
					
			self.common_wid.setChecked(True)
			self.common_wid.setEnabled(True)
		
		
# 		Required Widgets
# 		Setting ToolTips
# 		Styling of each widget			
# 		Resizing 		
# 		Grouping Radio Buttons			
# 		Layouts and Arrangement			
# 		setting the widget layout		
# 		Widget Background Styling	
# 		internal configurations		
		
# class phase_type(QtGui.QWidget):
# 	def __init__(self):
# 		super(phase_type,self).__init__()
# 		self.phase_type_lay = QtGui.QGridLayout()
# 		
# 		self.title = QtGui.QLabel('PHASE TYPE')
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.title.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 
# 		self.val1 = QtGui.QRadioButton('Explicitly defined AMB')
# 		self.val1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.val2 = QtGui.QRadioButton('LED without Auto AMBs')
# 		self.val2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.val3 = QtGui.QRadioButton('LED with Auto AMBs')
# 		self.val3.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		self.val1.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.val2.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")										
# 		
# 		self.val3.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		
# 		self.val3_op1 = QtGui.QRadioButton('None')
# 		self.val3_op2 = QtGui.QRadioButton('Pre AMB')
# 		self.val3_op3 = QtGui.QRadioButton('Pre and Post AMB')
# 		self.val3_op1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.val3_op2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.val3_op3.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.val3_op1.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 		self.val3_op2.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 																								
# 		self.val3_op3.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 		self.main_grp = QtGui.QButtonGroup()
# 		self.main_grp.addButton(self.val1)
# 		self.main_grp.addButton(self.val2)
# 		self.main_grp.addButton(self.val3)
# 		
# 		self.main_lay = QtGui.QVBoxLayout()
# 		self.main_lay.addWidget(self.val1)
# 		self.main_lay.addWidget(self.val2)
# 		self.main_lay.addWidget(self.val3)
# 		
# 		self.sub_grp = QtGui.QButtonGroup()
# 		self.sub_grp.addButton(self.val3_op1)
# 		self.sub_grp.addButton(self.val3_op2)
# 		self.sub_grp.addButton(self.val3_op3)
# 		
# 		self.sub_lay = QtGui.QVBoxLayout()
# 		self.sub_lay.addWidget(self.val3_op1)
# 		self.sub_lay.addWidget(self.val3_op2)
# 		self.sub_lay.addWidget(self.val3_op3)
# 		
# 		self.phase_type_lay.addWidget(self.title,0,0)
# 		self.phase_type_lay.addWidget(self.val1,1,0,1,2)
# 		self.phase_type_lay.addWidget(self.val2,2,0,2,2)
# 		self.phase_type_lay.addWidget(self.val3,3,0,3,2)
# 		
# 		self.phase_type_lay.addWidget(self.val3_op1,5,1)
# 		self.phase_type_lay.addWidget(self.val3_op2,6,1)
# 		self.phase_type_lay.addWidget(self.val3_op3,7,1)
# 		
# 		self.phase_type_lay2 = QtGui.QVBoxLayout()
# 		self.phase_type_lay2.addWidget(self.title,2)
# 		self.phase_type_lay2.addWidget(self.val1,2)
# 		self.phase_type_lay2.addWidget(self.val2,2)
# 		self.phase_type_lay2.addWidget(self.val3,2)
# 		
# 		self.phase_type_lay3 = QtGui.QVBoxLayout()
# 		self.phase_type_lay3.addWidget(self.val3_op1)
# 		self.phase_type_lay3.addWidget(self.val3_op2)
# 		self.phase_type_lay3.addWidget(self.val3_op3)
# 		
# 		self.phase_type_lay4 = QtGui.QHBoxLayout()
# 		self.phase_type_lay4.addWidget(Color('#f7f7f7'),1)
# 		self.phase_type_lay4.addLayout(self.phase_type_lay3,2)
# 		
# 		self.phase_type_lay2.addLayout(self.phase_type_lay4)
# 		self.setLayout(self.phase_type_lay2)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 
# 		self.setPalette(palette)			
# 		
# 		

# class transmitter_config(QtGui.QWidget):
# 	def __init__(self):
# 		super(transmitter_config,self).__init__()
# 		self.title = QtGui.QLabel('TRANSMITTER')
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.title.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.LedOn = QtGui.QLabel('LED ON Time')
# 		self.LedOn.setWordWrap(True)
# 		self.LedOn.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.LedOn.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
# 		self.LedOn.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.FilterSet = QtGui.QLabel('Filter Set Selected')
# 		self.FilterSet.setWordWrap(True)
# 		self.FilterSet.setAlignment(QtCore.Qt.AlignCenter)
# 		self.FilterSet.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.FilterSet.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		
# 		self.DRV_TXP = QtGui.QLabel('DRV_TXP')		
# 		self.DRV_TXP.setWordWrap(True)
# 		self.DRV_TXP.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.DRV_TXP.setAlignment(QtCore.Qt.AlignCenter)
# 		self.DRV_TXP.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.DRV_TXN1 = QtGui.QLabel('DRV_TXN1')
# 		self.DRV_TXN1.setWordWrap(True)
# 		self.DRV_TXN1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.DRV_TXN1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.DRV_TXN1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 
# 		self.DRV_TXN2 = QtGui.QLabel('DRV_TXN2')	
# 		self.DRV_TXN2.setWordWrap(True)	
# 		self.DRV_TXN2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.DRV_TXN2.setAlignment(QtCore.Qt.AlignCenter)
# 		self.DRV_TXN2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.ILED_DRV1 = QtGui.QLabel('ILED_DRV1 (mA)')
# 		self.ILED_DRV1.setWordWrap(True)	
# 		self.ILED_DRV1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.ILED_DRV1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.ILED_DRV1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.ILED_DRV2 = QtGui.QLabel('ILED_DRV2 (mA)')
# 		self.ILED_DRV2.setWordWrap(True)	
# 		self.ILED_DRV2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.ILED_DRV2.setAlignment(QtCore.Qt.AlignCenter)
# 		self.ILED_DRV2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.LedOnCombo = QtGui.QComboBox()
# 		self.LedOnCombo.addItems(['LED 1','LED 2'])
# 		self.LedOnCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.DRV_TXPCombo = QtGui.QComboBox()
# 		self.DRV_TXPCombo.addItems(['TXP1','TXP2','TXP3','TXP4'])
# 		self.DRV_TXPCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.DRV_TXN1Combo = QtGui.QComboBox()
# 		self.DRV_TXN1Combo.addItems(['TXN1','TXN2','TXN3','TXN4','TXN5','TXN6','TXN7','TXN8'])
# 		self.DRV_TXN1Combo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 
# 		self.DRV_TXN2Combo = QtGui.QComboBox()
# 		self.DRV_TXN2Combo.addItems(['TXN1','TXN2','TXN3','TXN4','TXN5','TXN6','TXN7','TXN8'])
# 		self.DRV_TXN2Combo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.userval1 = QtGui.QLineEdit()
# 		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.userval1.setSizePolicy(sizePolicy)
# 		self.userval1.setPlaceholderText('in mA')
# 		self.userval1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.userval2 = QtGui.QLineEdit()
# 		sizePolicy2 = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.userval2.setSizePolicy(sizePolicy2)
# 		self.userval2.setPlaceholderText('in mA')
# 		self.userval2.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		
# 		self.LedOnForm = QtGui.QHBoxLayout()
# 		self.LedOnForm.addWidget(self.LedOn,4)
# 		self.LedOnForm.addWidget(self.LedOnCombo,1)
# 		
# 		self.DRV_TXPForm = QtGui.QHBoxLayout()
# 		self.DRV_TXPForm.addWidget(self.DRV_TXP,3)
# 		self.DRV_TXPForm.addWidget(self.DRV_TXPCombo,1)
# 		
# 		self.DRV_TXN1Form = QtGui.QHBoxLayout()
# 		self.DRV_TXN1Form.addWidget(self.DRV_TXN1,3)
# 		self.DRV_TXN1Form.addWidget(self.DRV_TXN1Combo,1)
# 		
# 		self.DRV_TXN2Form = QtGui.QHBoxLayout()
# 		self.DRV_TXN2Form.addWidget(self.DRV_TXN2,3)
# 		self.DRV_TXN2Form.addWidget(self.DRV_TXN2Combo,1)
# 	
# 		self.ILED_DRV1Form = QtGui.QHBoxLayout()
# 		self.ILED_DRV1Form.addWidget(self.ILED_DRV1,3)
# 		self.ILED_DRV1Form.addWidget(self.userval1,1)
# 
# 		self.ILED_DRV2Form = QtGui.QHBoxLayout()
# 		self.ILED_DRV2Form.addWidget(self.ILED_DRV2,3)
# 		self.ILED_DRV2Form.addWidget(self.userval2,1)
# 
# 		self.transmitter_config_lay = QtGui.QVBoxLayout()
# 		
# 		self.transmitter_config_lay.addWidget(self.title)
# 		self.transmitter_config_lay.addLayout(self.LedOnForm)
# 		self.transmitter_config_lay.addWidget(self.FilterSet)
# 		self.transmitter_config_lay.addLayout(self.DRV_TXPForm)
# 		self.transmitter_config_lay.addLayout(self.DRV_TXN1Form)
# 		self.transmitter_config_lay.addLayout(self.DRV_TXN2Form)
# 		self.transmitter_config_lay.addLayout(self.ILED_DRV1Form)
# 		self.transmitter_config_lay.addLayout(self.ILED_DRV2Form)
# 		
# 		self.setLayout(self.transmitter_config_lay)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window,QtGui.QColor('#f7f7f7'))
# 
# 		self.setPalette(palette)

# class tia_config(QtGui.QWidget):
# 	def __init__(self):
# 		super(tia_config,self).__init__()
# 		self.title =  QtGui.QLabel('TIA n')
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.title.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.subTitle_PD = QtGui.QLabel('PDs connected to TIA : ')
# 		self.subTitle_PD.setStyleSheet("background: #f7f7f7; color:  rgba(0,124,140);border-bottom-width: 1px; border-bottom-style: solid; border-radius: 0px")
# 		self.subTitle_PD.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.subTitle_PD.setAlignment(QtCore.Qt.AlignCenter)
# 		self.PD1_checkbox = QtGui.QCheckBox('PD1')
# 		self.PD1_checkbox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.PD2_checkbox = QtGui.QCheckBox('PD2')
# 		self.PD2_checkbox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.PD3_checkbox = QtGui.QCheckBox('PD3')
# 		self.PD3_checkbox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.PD4_checkbox = QtGui.QCheckBox('PD4')
# 		self.PD4_checkbox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 				
# 		self.RF_label = QtGui.QLabel('RF')
# 		self.RF_label.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.RF_label.setAlignment(QtCore.Qt.AlignCenter)
# 		self.RF_label.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		self.RF_Combo = QtGui.QComboBox()
# 		self.RF_Combo.addItems(['3.7 KOhm','5 KOhm','10 KOhm','25 KOhm','33.3 KOhm','50 KOhm','71.5 KOhm','100 KOhm','142 KOhm','166 KOhm','200 KOhm','250 KOhm','500 KOhm','1 MOhm'])
# 		self.RF_Combo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		self.CF_ValLabel = QtGui.QLabel('Assigned CF')
# 		self.CF_ValLabel.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.CF_ValLabel.setAlignment(QtCore.Qt.AlignCenter)
# 		self.CF_ValLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		ioffdac_str = 'IOFFDAC_LED (' + unichr(int('b5',16))+'A)'
# 		self.IOFFDAC_LEDLabel = QtGui.QLabel(ioffdac_str)
# 		self.IOFFDAC_LEDLabel.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.IOFFDAC_LEDLabel.setAlignment(QtCore.Qt.AlignCenter)
# 		self.IOFFDAC_LEDLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		place_holderText = 'in ' + unichr(int('b5',16)) +'A'
# 		self.IOFFDAC_userval = QtGui.QLineEdit()
# 		self.IOFFDAC_userval.setPlaceholderText(place_holderText)
# 		self.IOFFDAC_userval.setAlignment(QtCore.Qt.AlignCenter)
# 		self.IOFFDAC_userval.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		
# 		self.EnableDC = QtGui.QLabel('Enable LED DC\n Cancellation')
# 		self.EnableDC.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.EnableDC.setAlignment(QtCore.Qt.AlignCenter)
# 		self.EnableDC.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		
# 		self.EnableDCYes = QtGui.QRadioButton('Yes')
# 		self.EnableDCYes.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDCNo = QtGui.QRadioButton('No')
# 		self.EnableDCNo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDCYes.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.EnableDCNo.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.PD_GRID = QtGui.QGridLayout()
# 		self.PD_GRID.addWidget(self.PD1_checkbox,0,0)
# 		self.PD_GRID.addWidget(self.PD2_checkbox,0,1)
# 		self.PD_GRID.addWidget(self.PD3_checkbox,1,0)
# 		self.PD_GRID.addWidget(self.PD4_checkbox,1,1)
# 		
# 		self.RF_Form = QtGui.QHBoxLayout()
# 		self.RF_Form.addWidget(self.RF_label,3)
# 		self.RF_Form.addWidget(self.RF_Combo,1)
# 		
# 		self.IOFFDAC_Form = QtGui.QHBoxLayout()
# 		self.IOFFDAC_Form.addWidget(self.IOFFDAC_LEDLabel,3)
# 		self.IOFFDAC_Form.addWidget(self.IOFFDAC_userval,1)
# 		
# 		self.EnableDCbool = QtGui.QVBoxLayout()
# 		self.EnableDCbool.addWidget(self.EnableDCYes)
# 		self.EnableDCbool.addWidget(self.EnableDCNo)
# 		
# 		self.EnableDC_Form = QtGui.QHBoxLayout()
# 		self.EnableDC_Form.addWidget(self.EnableDC)
# 		self.EnableDC_Form.addLayout(self.EnableDCbool)
# 		
# 		self.tia_config_lay = QtGui.QGridLayout()
# 		self.tia_config_lay.addWidget(self.title,0,0)
# 		self.tia_config_lay.addWidget(self.subTitle_PD,1,0)
# 		self.tia_config_lay.addLayout(self.PD_GRID,2,0)
# 		self.tia_config_lay.addLayout(self.RF_Form,4,0)
# 		self.tia_config_lay.addWidget(self.CF_ValLabel,5,0)
# 		self.tia_config_lay.addLayout(self.IOFFDAC_Form,6,0)
# 		self.tia_config_lay.addLayout(self.EnableDC_Form,7,0)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 
# 		self.setPalette(palette)
# 		self.setLayout(self.tia_config_lay)

# 
# class receiver_config(QtGui.QWidget):
# 	def __init__(self):
# 		super(receiver_config,self).__init__()
# 		self.title = QtGui.QLabel('RECEIVER')
# 		self.title.setAlignment(QtCore.Qt.AlignLeft)
# 		self.title.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		
# 		self.NoofTIAs = QtGui.QLabel('No. of TIAs')
# 		self.NoofTIAs.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.NoofTIAs.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.NoofTIAs.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.NUMAV = QtGui.QLabel('NUMAV')
# 		self.NUMAV.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.NUMAV.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.NUMAV.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.SchemeforAMB = QtGui.QLabel('Scheme for AMB Cancellation')
# 		self.SchemeforAMB.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.SchemeforAMB.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.SchemeforAMB.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.FIFOCtrl = QtGui.QLabel('FIFO DATA CTRL')
# 		self.FIFOCtrl.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.FIFOCtrl.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.FIFOCtrl.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.MaskingFactor = QtGui.QLabel('Masking Factor')
# 		self.MaskingFactor.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.MaskingFactor.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.MaskingFactor.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.EnableDRE = QtGui.QLabel('Enable DRE')
# 		self.EnableDRE.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.EnableDRE.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDRE.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.DecimationFactor = QtGui.QLabel('Decimation Factor')
# 		self.DecimationFactor.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.DecimationFactor.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.DecimationFactor.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.NoofTIAsCombo = QtGui.QComboBox()
# 		self.no_ofTIAs = 4
# 		self.No_Of_TIAs = ['1','2','3','4']
# 		self.NoofTIAsCombo.addItems(self.No_Of_TIAs[0:self.no_ofTIAs])
# 		self.NoofTIAsCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.NoofTIAs_lay = QtGui.QHBoxLayout()
# 		self.NoofTIAs_lay.addWidget(self.NoofTIAs,3)
# 		self.NoofTIAs_lay.addWidget(self.NoofTIAsCombo,1)
# 		self.NoofTIAs_lay.addWidget(Color('#f7f7f7'),10)
# 		
# 		self.NUMAVCombo = QtGui.QComboBox()
# 		self.NUMAVCombo.addItems(['1','2','3','4','8'])
# 		self.NUMAVCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.NUMAV_lay = QtGui.QHBoxLayout()
# 		self.NUMAV_lay.addWidget(self.NUMAV,3)
# 		self.NUMAV_lay.addWidget(self.NUMAVCombo,1)
# 		self.NUMAV_lay.addWidget(Color('#f7f7f7'),10)
# 		
# 		self.SchemeforAMBCombo = QtGui.QComboBox()
# 		self.SchemeforAMBCombo.addItems(['AACM OFF','Estimate and Cancel AACM','Cancel AACM without Estimation'])
# 		self.SchemeforAMBCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.SchemeforAMB_lay = QtGui.QHBoxLayout()
# 		self.SchemeforAMB_lay.addWidget(self.SchemeforAMB,3)
# 		self.SchemeforAMB_lay.addWidget(self.SchemeforAMBCombo,1)
# 		self.SchemeforAMB_lay.addWidget(Color('#f7f7f7'),2)
# 		
# 		self.EnableDRE_bool = QtGui.QFormLayout()
# 		self.EnableDRE_yes = QtGui.QRadioButton('YES')
# 		self.EnableDRE_yes.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDRE_no = QtGui.QRadioButton('NO')
# 		self.EnableDRE_no.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDRE_yes.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.EnableDRE_no.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 										
# 		self.EnableDRE_bool.addRow(self.EnableDRE_yes,self.EnableDRE_no)
# 		
# 		self.EnableDRE_bool_wid = QtGui.QWidget()
# 		self.EnableDRE_bool_wid.setLayout(self.EnableDRE_bool)
# 		
# # 		self.EnableDRE_lay = QtGui.QHBoxLayout()
# # 		self.EnableDRE_lay.addWidget(self.EnableDRE)
# # 		self.EnableDRE_lay.addWidget(self.EnableDRE_bool_wid)
# 		
# 		self.SchemeforAMB_lay.addWidget(self.EnableDRE,2)
# 		self.SchemeforAMB_lay.addWidget(self.EnableDRE_bool_wid,2)
# 		self.FIFOCtrlCombo = QtGui.QComboBox()
# 		self.FIFOCtrlCombo.addItems(['None'])
# 		self.FIFOCtrlForm = QtGui.QHBoxLayout()
# 		self.FIFOCtrlForm.addWidget(self.FIFOCtrl,3)
# 		self.FIFOCtrlForm.addWidget(self.FIFOCtrlCombo,4)
# 		
# 		self.MaskingFactorCombo = QtGui.QComboBox()
# 		self.MaskingFactorCombo.addItems(['None'])
# 		self.MaskingFactorForm = QtGui.QHBoxLayout()
# 		self.FIFOCtrlForm.addWidget(self.MaskingFactor,3)
# 		self.FIFOCtrlForm.addWidget(self.MaskingFactorCombo,4)
# 		
# 		self.DecimationFactorCombo = QtGui.QComboBox()
# 		self.DecimationFactorCombo.addItems(['NO Decimation','Decimation by 2','Decimation by 4','Decimation by 8','Decimation by 16','Decimation by 32'])
# 		self.DecimationFactorForm = QtGui.QHBoxLayout()
# 		self.FIFOCtrlForm.addWidget(self.DecimationFactor,5)
# 		self.FIFOCtrlForm.addWidget(self.DecimationFactorCombo,1)
# 		
# 		self.receiver_config_lay = QtGui.QVBoxLayout()
# 	
# # 		self.receiver_config_lay.addWidget(self.title,0,0)
# # 		self.receiver_config_lay.addLayout(self.NoofTIAs_lay,1,0)
# # 		self.receiver_config_lay.addLayout(self.NUMAV_lay,2,0)
# # 		self.receiver_config_lay.addLayout(self.SchemeforAMB_lay,3,0,3,1)
# # 		self.receiver_config_lay.addLayout(self.EnableDRE_lay,3,2)
# # 		self.receiver_config_lay.addLayout(self.FIFOCtrlForm,4,0)
# # 		self.receiver_config_lay.addLayout(self.MaskingFactorForm,4,1)
# # 		self.receiver_config_lay.addLayout(self.DecimationFactorForm,4,2)
# 		
# 		self.receiver_config_lay.addWidget(self.title)
# 		self.receiver_config_lay.addLayout(self.NoofTIAs_lay)
# 		self.receiver_config_lay.addLayout(self.NUMAV_lay)
# 		self.receiver_config_lay.addLayout(self.SchemeforAMB_lay)
# # 		self.receiver_config_lay.addLayout(self.EnableDRE_lay)
# 		self.receiver_config_lay.addLayout(self.FIFOCtrlForm)
# # 		self.receiver_config_lay.addLayout(self.MaskingFactorForm)
# # 		self.receiver_config_lay.addLayout(self.DecimationFactorForm)
# 		
# 		self.tia1 = tia_config()
# 		self.tia1.title.setText('TIA1')
# 		self.tia2 = tia_config()
# 		self.tia2.title.setText('TIA2')
# 		self.tia3 = tia_config()
# 		self.tia3.title.setText('TIA3')
# 		self.tia4 = tia_config()
# 		self.tia4.title.setText('TIA4')
# 	
# 		self.tiaN_grid = QtGui.QHBoxLayout()
# 		self.tiaN_grid.addWidget(self.tia1,1)
# 		self.tiaN_grid.addWidget(self.tia2,1)
# 		self.tiaN_grid.addWidget(self.tia3,1)
# 		self.tiaN_grid.addWidget(self.tia4,1)
# 		
# 		self.receiver_config_main = QtGui.QVBoxLayout()
# 		self.receiver_config_main.addLayout(self.receiver_config_lay,2)
# 		self.receiver_config_main.addLayout(self.tiaN_grid,3)
# 				
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 
# 		self.setPalette(palette)
# 
# 		self.setLayout(self.receiver_config_main)
#
# class control_layout(QtGui.QWidget):
# 	def __init__(self):
# 		super(control_layout,self).__init__()
# 		
# 		self.individual = QtGui.QRadioButton('Individual')
# 		self.summary = QtGui.QRadioButton('Summary')
# 		self.individual.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.summary.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.individual.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 		self.summary.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 										
# 		self.view_layout1 = QtGui.QVBoxLayout()
# 		self.view_layout1.addWidget(self.individual)
# 		self.view_layout1.addWidget(self.summary)
# 		
# 		self.viewLabel = QtGui.QLabel('View')
# 		self.viewLabel.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.viewLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.view_layout =  QtGui.QFormLayout()
# # 		self.view_layout.addWidget(self.viewLabel,2)
# # 		self.view_layout.addLayout(self.view_layout1,3)
# 		self.view_layout.addRow(self.viewLabel,self.view_layout1)
# 		self.common_phN = QtGui.QHBoxLayout()
# 		self.ph1_8 = QtGui.QHBoxLayout()
# 		self.ph9_16 = QtGui.QHBoxLayout()
# 		self.phN = QtGui.QVBoxLayout()
# 		
# 		self.phN_arr = []
# 		for i in range(16):
# 			ph_str = 'PH' + str(i)
# 			self.phN_arr.append(QtGui.QRadioButton(ph_str))
# 			
# 		for i in range(8):
# 			self.phN_arr[i].setFixedWidth(70)
# 			self.phN_arr[i].setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 			self.ph1_8.addWidget(self.phN_arr[i])
# 			self.phN_arr[i].setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		for i in range(8):
# 			self.phN_arr[i+8].setFixedWidth(70)
# 			self.phN_arr[i+8].setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 			self.ph9_16.addWidget(self.phN_arr[i+8])
# 			self.phN_arr[i+1].setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 			
# 		self.phN.addLayout(self.ph1_8)
# 		self.phN.addLayout(self.ph9_16)
# 		
# 		self.common_wid = QtGui.QRadioButton('Common')
# 		self.common_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.common_wid.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 										
# # 		self.common_phN.addRow(self.common_wid,self.phN)
# 		self.common_phN.addWidget(self.common_wid)
# 		self.common_phN.addLayout(self.phN)
# 		
# 		self.common_ph_group = QtGui.QButtonGroup()
# 		self.common_ph_group.addButton(self.common_wid)
# 		for i in range(16):
# 			self.common_ph_group.addButton(self.phN_arr[i])
# 			
# 		self.req_ph_lay = QtGui.QFormLayout()
# 		self.userval1 = QtGui.QLineEdit()
# 		self.label1 = QtGui.QLabel('Required \nNo. of Phases')
# # 		self.userval1.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
# 		self.label1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.userval1.setSizePolicy(sizePolicy)
# 	
# 		self.label1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.label1.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.userval1.setAlignment(QtCore.Qt.AlignCenter)
# # 		self.userval1.setFixedWidth(40)
# 
# 		self.req_ph_lay.addRow(self.label1,self.userval1)		
# 		
# 		self.control_lay = QtGui.QHBoxLayout()
# 		self.control_lay.addLayout(self.req_ph_lay)
# 		self.control_lay.addLayout(self.common_phN)
# 		self.control_lay.addLayout(self.view_layout)
# 		
# 		self.individual.setChecked(True)
# 		
# # 		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 		self.setPalette(palette)
# 		self.setLayout(self.control_lay)
