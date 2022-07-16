import math

# configuration of required Global Parameters

# configuration of Number of Phases Required
def AFE_config_numOfPhases(noOfPhases):
	AFE_modifyRegGlobal(dev1.Page0.REG_NUMPHASE_PPG,     noOfPhases-1)
	No_of_Phases_PerPhase[0] = noOfPhases
	logWindow_wid.settingLogText("Total of "+str(noOfPhases)+" Phases are set")
	
# Transmitter configurations
# filter set selection anf LED ON Time Selection
def AFE_config_FilterSetSel(PhNo,filter_Set_Select):
	# selecting which filter set to be used 
	# 0 for Set1 & 1 for Set2
	AFE_modifyRegPPM(PhNo, dev1.Page1.FILTER_SET_SEL, filter_Set_Select)

def AFE_config_LEDOnTime_width(PhNo,ledOnWidth,filterNo):
	#(REG_TWLED + 1)*tTE
	
	AFE_modifyRegPPM(PhNo, dev1.Page1.REG_TWLED, ledOnWidth-1)
# 	AFE_config_FilterSetSel(PhNo,filterNo)
	
# 	if ledOnNum == 1:
# 		
# 		AFE_config_FilterSetSel(PhNo,0)		
# 		AFE_modifyRegPPM(PhNo, dev1.Page1.REG_TWLED, LED1_ON_TIME_GLOBAL[0]-1)
# # 		logWindow_wid.settingLogText('LED 1 and Filter Set 1 are chosen')
# 	elif ledOnNum == 2:
# 		AFE_config_FilterSetSel(PhNo,1)		
# 		AFE_modifyRegPPM(PhNo, dev1.Page1.REG_TWLED, LED2_ON_TIME_GLOBAL[0]-1)
# # 		logWindow_wid.settingLogText('LED 2 and Filter Set 2 are chosen')
		
		
# 		TXP Driver configuration
def AFE_config_Drv_TXP(PhNo,drv_txp):

	AFE_modifyRegPPM(PhNo, dev1.Page1.LED_DRV_TXP,       drv_txp)
	
def AFE_config_Drv1_TXN(PhNo,drv_txn):

	AFE_modifyRegPPM(PhNo, dev1.Page1.LED_DRV1_TXN,      drv_txn)

def AFE_config_Drv2_TXN(PhNo,drv_txn):

	AFE_modifyRegPPM(PhNo, dev1.Page1.LED_DRV2_TXN,      drv_txn)
	
	
def AFE_config_ILED_DRV1(PhNo,ledDrvCurr):
	# sets the LED Driver 1 current
	maxCurr = FS_LED_CURRENT_global[0]
	
# 	oneLSBCurr = maxCurr/(pow(2,8)-1)
	oneLSBCurr = 0.098
# 	logWindow_wid.settingLogText('came here'+ str(ledDrvCurr)+'  ' + str(FS_LED_CURRENT_global[0])+ str(oneLSBCurr))
	
	ILEDdrv_curr = ledDrvCurr/oneLSBCurr

	if ILEDdrv_curr < math.floor(ILEDdrv_curr)+oneLSBCurr:
		ILEDdrv_curr = math.floor(ILEDdrv_curr)
	else:
		ILEDdrv_curr = math.ceil(ILEDdrv_curr)
	
	if ILEDdrv_curr>255:
		AFE_modifyRegPPM(PhNo, dev1.Page1.ILED_DRV1, 0)
		return
	AFE_modifyRegPPM(PhNo, dev1.Page1.ILED_DRV1, ILEDdrv_curr)
# 	logWindow_wid.settingLogText('came here too')

def AFE_config_ILED_DRV2(PhNo,ledDrvCurr):
	# sets the LED Driver 2 current
	maxCurr = FS_LED_CURRENT_global[0]
# 	oneLSBCurr = float(maxCurr/(pow(2,8)-1))
	oneLSBCurr = 0.098
	
	
	ILEDdrv_curr = ledDrvCurr/oneLSBCurr

	if ILEDdrv_curr < math.floor(ILEDdrv_curr)+oneLSBCurr:
		ILEDdrv_curr = math.floor(ILEDdrv_curr)
	else:
		ILEDdrv_curr = math.ceil(ILEDdrv_curr)
	
	if ILEDdrv_curr>255:
		AFE_modifyRegPPM(PhNo, dev1.Page1.ILED_DRV2, 0)
		return
	AFE_modifyRegPPM(PhNo, dev1.Page1.ILED_DRV2, ILEDdrv_curr)
# 	logWindow_wid.settingLogText('came here too')
