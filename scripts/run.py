import os
from pyspark import SparkConf,SparkContext
from pyspark.sql import SQLContext,HiveContext

from pyspark.sql.functions import udf
from pyspark.sql.types import *


import json

import sys

conf = (SparkConf()
  .setAppName("data_import")
  .set("spark.shuffle.service.enabled","true"))
  

sc = SparkContext(conf = conf)

sqlContext= SQLContext(sc)

cat_main = json.dumps({"table":{"namespace":"default", "name":"tim_ericcson_bulk", "tablecoder":"primitivetype"},"rowkey":"rowkey","columns":{"rowkey":{"cf":"rowkey", "col":"rowkey","type":"string"},\
"client":{"cf":"ericcson","col":"client","type":"string"},\
"area":{"cf":"ericcson","col":"area","type":"string"},\
"recordtype":{"cf":"ericcson","col":"recordtype","type":"string"},\
"servedimsi":{"cf":"ericcson","col":"servedimsi","type":"string"},\
"ggsnaddress_ipbinv4address":{"cf":"ericcson","col":"ggsnaddress_ipbinv4address","type":"string"},\
"chargingid":{"cf":"ericcson","col":"chargingid","type":"string"},\
"sgsnaddress_ipbinv4address":{"cf":"ericcson","col":"sgsnaddress_ipbinv4address","type":"string"},\
"accesspointnameni":{"cf":"ericcson","col":"accesspointnameni","type":"string"},\
"pdptype":{"cf":"ericcson","col":"pdptype","type":"string"},\
"servedpdpaddr_ipbinv4address":{"cf":"ericcson","col":"servedpdpaddr_ipbinv4address","type":"string"},\
"dynamicaddressflag":{"cf":"ericcson","col":"dynamicaddressflag","type":"string"},\
"lotv_qosnegotiated":{"cf":"ericcson","col":"lotv_qosnegotiated","type":"string"},\
"lotv_datavolumegprsuplink":{"cf":"ericcson","col":"lotv_datavolumegprsuplink","type":"string"},\
"lotv_datavolumegprsdownlink":{"cf":"ericcson","col":"lotv_datavolumegprsdownlink","type":"string"},\
"lotv_changecondition":{"cf":"ericcson","col":"lotv_changecondition","type":"string"},\
"lotv_changetime":{"cf":"ericcson","col":"lotv_changetime","type":"string"},\
"lotf_uli_flag":{"cf":"ericcson","col":"lotf_uli_flag","type":"string"},\
"lotf_uli_mcc":{"cf":"ericcson","col":"lotf_uli_mcc","type":"string"},\
"lotf_uli_mnc":{"cf":"ericcson","col":"lotf_uli_mnc","type":"string"},\
"lotf_uli_lac":{"cf":"ericcson","col":"lotf_uli_lac","type":"string"},\
"lotf_uli_cell":{"cf":"ericcson","col":"lotf_uli_cell","type":"string"},\
"lotf_uli_eci":{"cf":"ericcson","col":"lotf_uli_eci","type":"string"},\
"lotf_uli_mcc_2":{"cf":"ericcson","col":"lotf_uli_mcc_2","type":"string"},\
"lotf_uli_mnc_2":{"cf":"ericcson","col":"lotf_uli_mnc_2","type":"string"},\
"lotf_uli_eci_2":{"cf":"ericcson","col":"lotf_uli_eci_2","type":"string"},\
"lotv_epcqosi_qci":{"cf":"ericcson","col":"lotv_epcqosi_qci","type":"string"},\
"lotv_epcqosi_maxrequbandwithul":{"cf":"ericcson","col":"lotv_epcqosi_maxrequbandwithul","type":"string"},\
"lotv_epcqosi_maxrequbandwithdl":{"cf":"ericcson","col":"lotv_epcqosi_maxrequbandwithdl","type":"string"},\
"lotv_epcqosi_guarantbitrateul":{"cf":"ericcson","col":"lotv_epcqosi_guarantbitrateul","type":"string"},\
"lotv_epcqosi_guarantbitratedl":{"cf":"ericcson","col":"lotv_epcqosi_guarantbitratedl","type":"string"},\
"lotv_epcqosi_arp":{"cf":"ericcson","col":"lotv_epcqosi_arp","type":"string"},\
"recordopeningtime":{"cf":"ericcson","col":"recordopeningtime","type":"string"},\
"duration":{"cf":"ericcson","col":"duration","type":"string"},\
"causeforrecclosing":{"cf":"ericcson","col":"causeforrecclosing","type":"string"},\
"recordsequencenumber":{"cf":"ericcson","col":"recordsequencenumber","type":"string"},\
"nodeid":{"cf":"ericcson","col":"nodeid","type":"string"},\
"recordextensions_identifier":{"cf":"ericcson","col":"recordextensions_identifier","type":"string"},\
"recordextensions_significance":{"cf":"ericcson","col":"recordextensions_significance","type":"string"},\
"rc_changetime":{"cf":"ericcson","col":"rc_changetime","type":"string"},\
"rc_ls_serviceidentifier":{"cf":"ericcson","col":"rc_ls_serviceidentifier","type":"string"},\
"rc_ls_voluplink":{"cf":"ericcson","col":"rc_ls_voluplink","type":"string"},\
"rc_ls_voldownlink":{"cf":"ericcson","col":"rc_ls_voldownlink","type":"string"},\
"rc_lc_serviceclass":{"cf":"ericcson","col":"rc_lc_serviceclass","type":"string"},\
"rc_lc_voluplink":{"cf":"ericcson","col":"rc_lc_voluplink","type":"string"},\
"rc_lc_voldownlink":{"cf":"ericcson","col":"rc_lc_voldownlink","type":"string"},\
"rc_lc_volrateup_valuedigits":{"cf":"ericcson","col":"rc_lc_volrateup_valuedigits","type":"string"},\
"rc_lc_volrateup_exponent":{"cf":"ericcson","col":"rc_lc_volrateup_exponent","type":"string"},\
"rc_lc_volratedown_valuedigits":{"cf":"ericcson","col":"rc_lc_volratedown_valuedigits","type":"string"},\
"rc_lc_volratedown_exponent":{"cf":"ericcson","col":"rc_lc_volratedown_exponent","type":"string"},\
"rc_lc_sespol_vollimitaction":{"cf":"ericcson","col":"rc_lc_sespol_vollimitaction","type":"string"},\
"rc_lc_sespol_blocklimitaction":{"cf":"ericcson","col":"rc_lc_sespol_blocklimitaction","type":"string"},\
"rc_lc_blockitem_blocks":{"cf":"ericcson","col":"rc_lc_blockitem_blocks","type":"string"},\
"rc_lc_blockitem_blockrate":{"cf":"ericcson","col":"rc_lc_blockitem_blockrate","type":"string"},\
"rc_lc_blockitem_blocksize":{"cf":"ericcson","col":"rc_lc_blockitem_blocksize","type":"string"},\
"rc_lc_blockitem_blocksizetype":{"cf":"ericcson","col":"rc_lc_blockitem_blocksizetype","type":"string"},\
"rc_lc_blockitem_starttime":{"cf":"ericcson","col":"rc_lc_blockitem_starttime","type":"string"},\
"rc_lc_blockitem_stoptime":{"cf":"ericcson","col":"rc_lc_blockitem_stoptime","type":"string"},\
"rc_initialcharge":{"cf":"ericcson","col":"rc_initialcharge","type":"string"},\
"rc_sessionpolicy":{"cf":"ericcson","col":"rc_sessionpolicy","type":"string"},\
"rc_blockitem_blocks":{"cf":"ericcson","col":"rc_blockitem_blocks","type":"string"},\
"rc_blockitem_blockrate":{"cf":"ericcson","col":"rc_blockitem_blockrate","type":"string"},\
"rc_blockitem_blocksize":{"cf":"ericcson","col":"rc_blockitem_blocksize","type":"string"},\
"rc_blockitem_blocksizetype":{"cf":"ericcson","col":"rc_blockitem_blocksizetype","type":"string"},\
"rc_blockitem_starttime":{"cf":"ericcson","col":"rc_blockitem_starttime","type":"string"},\
"rc_blockitem_stoptime":{"cf":"ericcson","col":"rc_blockitem_stoptime","type":"string"},\
"rr_crcontrolenabled":{"cf":"ericcson","col":"rr_crcontrolenabled","type":"string"},\
"rr_ccspeer":{"cf":"ericcson","col":"rr_ccspeer","type":"string"},\
"rr_crunit_unittype":{"cf":"ericcson","col":"rr_crunit_unittype","type":"string"},\
"rr_crunit_currencycode":{"cf":"ericcson","col":"rr_crunit_currencycode","type":"string"},\
"rr_crcontroldiagnostics":{"cf":"ericcson","col":"rr_crcontroldiagnostics","type":"string"},\
"rr_crdeniedaction":{"cf":"ericcson","col":"rr_crdeniedaction","type":"string"},\
"rr_crcontrolfailureaction":{"cf":"ericcson","col":"rr_crcontrolfailureaction","type":"string"},\
"rr_crcfr_requesttype":{"cf":"ericcson","col":"rr_crcfr_requesttype","type":"string"},\
"rr_crcfr_requeststatus":{"cf":"ericcson","col":"rr_crcfr_requeststatus","type":"string"},\
"rr_crcfr_resultcode":{"cf":"ericcson","col":"rr_crcfr_resultcode","type":"string"},\
"rr_crcfr_recordnumber":{"cf":"ericcson","col":"rr_crcfr_recordnumber","type":"string"},\
"rr_crcfr_starttime":{"cf":"ericcson","col":"rr_crcfr_starttime","type":"string"},\
"rr_crcfr_stoptime":{"cf":"ericcson","col":"rr_crcfr_stoptime","type":"string"},\
"rr_crcfr_lastcrg_valuedigits":{"cf":"ericcson","col":"rr_crcfr_lastcrg_valuedigits","type":"string"},\
"rr_crcfr_lastcrg_exponent":{"cf":"ericcson","col":"rr_crcfr_lastcrg_exponent","type":"string"},\
"rr_crcfr_crused_valuedigits":{"cf":"ericcson","col":"rr_crcfr_crused_valuedigits","type":"string"},\
"rr_crcfr_crused_exponent":{"cf":"ericcson","col":"rr_crcfr_crused_exponent","type":"string"},\
"rr_crcfr_newcrcontrolsessionid":{"cf":"ericcson","col":"rr_crcfr_newcrcontrolsessionid","type":"string"},\
"rr_crcfr_defcrused_valuedigits":{"cf":"ericcson","col":"rr_crcfr_defcrused_valuedigits","type":"string"},\
"rr_crcfr_defcrused_exponent":{"cf":"ericcson","col":"rr_crcfr_defcrused_exponent","type":"string"},\
"rr_crcfr_ccrequestnumber":{"cf":"ericcson","col":"rr_crcfr_ccrequestnumber","type":"string"},\
"rr_crcontrolsessionid":{"cf":"ericcson","col":"rr_crcontrolsessionid","type":"string"},\
"rr_ccsrealm":{"cf":"ericcson","col":"rr_ccsrealm","type":"string"},\
"rp_policycontrolenabled":{"cf":"ericcson","col":"rp_policycontrolenabled","type":"string"},\
"rp_pcspeer":{"cf":"ericcson","col":"rp_pcspeer","type":"string"},\
"rp_policycontroldiagnostics":{"cf":"ericcson","col":"rp_policycontroldiagnostics","type":"string"},\
"rp_policycontrolfailureaction":{"cf":"ericcson","col":"rp_policycontrolfailureaction","type":"string"},\
"rp_pcfr_requesttype":{"cf":"ericcson","col":"rp_pcfr_requesttype","type":"string"},\
"rp_pcfr_requeststatus":{"cf":"ericcson","col":"rp_pcfr_requeststatus","type":"string"},\
"rp_pcfr_resultcode":{"cf":"ericcson","col":"rp_pcfr_resultcode","type":"string"},\
"rp_pcfr_sessionid":{"cf":"ericcson","col":"rp_pcfr_sessionid","type":"string"},\
"rp_pcfr_starttime":{"cf":"ericcson","col":"rp_pcfr_starttime","type":"string"},\
"rp_pcfr_stoptime":{"cf":"ericcson","col":"rp_pcfr_stoptime","type":"string"},\
"rp_currencycode":{"cf":"ericcson","col":"rp_currencycode","type":"string"},\
"rp_pcsrealm":{"cf":"ericcson","col":"rp_pcsrealm","type":"string"},\
"rp_policycontrolsessionid":{"cf":"ericcson","col":"rp_policycontrolsessionid","type":"string"},\
"r_usercategory":{"cf":"ericcson","col":"r_usercategory","type":"string"},\
"r_rulespaceid":{"cf":"ericcson","col":"r_rulespaceid","type":"string"},\
"rs_ratinggroup":{"cf":"ericcson","col":"rs_ratinggroup","type":"string"},\
"rs_serviceidentifier":{"cf":"ericcson","col":"rs_serviceidentifier","type":"string"},\
"rs_localsequencenumber":{"cf":"ericcson","col":"rs_localsequencenumber","type":"string"},\
"rs_method":{"cf":"ericcson","col":"rs_method","type":"string"},\
"rs_inactivity":{"cf":"ericcson","col":"rs_inactivity","type":"string"},\
"rs_resolution":{"cf":"ericcson","col":"rs_resolution","type":"string"},\
"rs_ccrequestnumber":{"cf":"ericcson","col":"rs_ccrequestnumber","type":"string"},\
"rs_servicespecificunits":{"cf":"ericcson","col":"rs_servicespecificunits","type":"string"},\
"rs_listofuri_count":{"cf":"ericcson","col":"rs_listofuri_count","type":"string"},\
"rs_listofuri_uri":{"cf":"ericcson","col":"rs_listofuri_uri","type":"string"},\
"rt_ratinggroup":{"cf":"ericcson","col":"rt_ratinggroup","type":"string"},\
"rt_starttime":{"cf":"ericcson","col":"rt_starttime","type":"string"},\
"rt_endtime":{"cf":"ericcson","col":"rt_endtime","type":"string"},\
"rt_datavolumeuplink":{"cf":"ericcson","col":"rt_datavolumeuplink","type":"string"},\
"rt_datavolumedownlink":{"cf":"ericcson","col":"rt_datavolumedownlink","type":"string"},\
"localsequencenumber":{"cf":"ericcson","col":"localsequencenumber","type":"string"},\
"apnselectionmode":{"cf":"ericcson","col":"apnselectionmode","type":"string"},\
"servedmsisdn":{"cf":"ericcson","col":"servedmsisdn","type":"string"},\
"chargingcharacteristics":{"cf":"ericcson","col":"chargingcharacteristics","type":"string"},\
"chchselectionmode":{"cf":"ericcson","col":"chchselectionmode","type":"string"},\
"imssignalingconstring":{"cf":"ericcson","col":"imssignalingconstring","type":"string"},\
"externalchargingid":{"cf":"ericcson","col":"externalchargingid","type":"string"},\
"sgsnplmnidentifier":{"cf":"ericcson","col":"sgsnplmnidentifier","type":"string"},\
"psfurnishcharginginformation":{"cf":"ericcson","col":"psfurnishcharginginformation","type":"string"},\
"servedimeisv":{"cf":"ericcson","col":"servedimeisv","type":"string"},\
"rattype":{"cf":"ericcson","col":"rattype","type":"string"},\
"mstimezone":{"cf":"ericcson","col":"mstimezone","type":"string"},\
"userlocationinformation_flag":{"cf":"ericcson","col":"userlocationinformation_flag","type":"string"},\
"userlocationinformation_mcc":{"cf":"ericcson","col":"userlocationinformation_mcc","type":"string"},\
"userlocationinformation_mnc":{"cf":"ericcson","col":"userlocationinformation_mnc","type":"string"},\
"userlocationinformation_lac":{"cf":"ericcson","col":"userlocationinformation_lac","type":"string"},\
"userlocationinformation_cell":{"cf":"ericcson","col":"userlocationinformation_cell","type":"string"},\
"userlocationinformation_eci":{"cf":"ericcson","col":"userlocationinformation_eci","type":"string"},\
"userlocationinformation_mcc_2":{"cf":"ericcson","col":"userlocationinformation_mcc_2","type":"string"},\
"userlocationinformation_mnc_2":{"cf":"ericcson","col":"userlocationinformation_mnc_2","type":"string"},\
"userlocationinformation_eci_2":{"cf":"ericcson","col":"userlocationinformation_eci_2","type":"string"},\
"listofservicedata_ratinggroup":{"cf":"ericcson","col":"listofservicedata_ratinggroup","type":"string"},\
"listofservicedata_resultcode":{"cf":"ericcson","col":"listofservicedata_resultcode","type":"string"},\
"losd_localsequencenumber":{"cf":"ericcson","col":"losd_localsequencenumber","type":"string"},\
"losd_timeoffirstusage":{"cf":"ericcson","col":"losd_timeoffirstusage","type":"string"},\
"losd_timeoflastusage":{"cf":"ericcson","col":"losd_timeoflastusage","type":"string"},\
"losd_timeusage":{"cf":"ericcson","col":"losd_timeusage","type":"string"},\
"losd_serviceconditionchange":{"cf":"ericcson","col":"losd_serviceconditionchange","type":"string"},\
"losd_qosinformationneg":{"cf":"ericcson","col":"losd_qosinformationneg","type":"string"},\
"losd_sgsn_address":{"cf":"ericcson","col":"losd_sgsn_address","type":"string"},\
"losd_sgsnplmnidentifier":{"cf":"ericcson","col":"losd_sgsnplmnidentifier","type":"string"},\
"losd_datavolumefbcuplink":{"cf":"ericcson","col":"losd_datavolumefbcuplink","type":"string"},\
"losd_datavolumefbcdownlink":{"cf":"ericcson","col":"losd_datavolumefbcdownlink","type":"string"},\
"losd_timeofreport":{"cf":"ericcson","col":"losd_timeofreport","type":"string"},\
"losd_rattype":{"cf":"ericcson","col":"losd_rattype","type":"string"},\
"losd_failurehandlingcontinue":{"cf":"ericcson","col":"losd_failurehandlingcontinue","type":"string"},\
"losd_serviceidentifier":{"cf":"ericcson","col":"losd_serviceidentifier","type":"string"},\
"losd_pfci_psfreeformatdata":{"cf":"ericcson","col":"losd_pfci_psfreeformatdata","type":"string"},\
"losd_pfci_psffdappendindicator":{"cf":"ericcson","col":"losd_pfci_psffdappendindicator","type":"string"},\
"losd_afrecordinformation":{"cf":"ericcson","col":"losd_afrecordinformation","type":"string"},\
"losd_qosin_qci":{"cf":"ericcson","col":"losd_qosin_qci","type":"string"},\
"losd_qosin_maxrequdbandwithul":{"cf":"ericcson","col":"losd_qosin_maxrequdbandwithul","type":"string"},\
"losd_qosin_maxrequdbandwithdl":{"cf":"ericcson","col":"losd_qosin_maxrequdbandwithdl","type":"string"},\
"losd_qosin_guaranteedbitrateul":{"cf":"ericcson","col":"losd_qosin_guaranteedbitrateul","type":"string"},\
"losd_qosin_guaranteedbitratedl":{"cf":"ericcson","col":"losd_qosin_guaranteedbitratedl","type":"string"},\
"losd_qosin_arp":{"cf":"ericcson","col":"losd_qosin_arp","type":"string"},\
"losd_sgsna_ipba_ipbinv4address":{"cf":"ericcson","col":"losd_sgsna_ipba_ipbinv4address","type":"string"},\
"losd_sgsna_ipba_ipbinv6address":{"cf":"ericcson","col":"losd_sgsna_ipba_ipbinv6address","type":"string"},\
"losd_sgsna_iptra_ipstringv4add":{"cf":"ericcson","col":"losd_sgsna_iptra_ipstringv4add","type":"string"},\
"losd_sgsna_iptra_ipstringv6add":{"cf":"ericcson","col":"losd_sgsna_iptra_ipstringv6add","type":"string"},\
"losd_userlocationinformation":{"cf":"ericcson","col":"losd_userlocationinformation","type":"string"},\
"losd_ebci_numberofevents":{"cf":"ericcson","col":"losd_ebci_numberofevents","type":"string"},\
"losd_ebci_eventtimestamps":{"cf":"ericcson","col":"losd_ebci_eventtimestamps","type":"string"},\
"servedimei":{"cf":"ericcson","col":"servedimei","type":"string"},\
"msnetworkcapability":{"cf":"ericcson","col":"msnetworkcapability","type":"string"},\
"routingarea":{"cf":"ericcson","col":"routingarea","type":"string"},\
"locationareacode":{"cf":"ericcson","col":"locationareacode","type":"string"},\
"cellidentifier":{"cf":"ericcson","col":"cellidentifier","type":"string"},\
"ggsnaddressused_ipbinv4address":{"cf":"ericcson","col":"ggsnaddressused_ipbinv4address","type":"string"},\
"lotv_qosrequested":{"cf":"ericcson","col":"lotv_qosrequested","type":"string"},\
"sgsnchange":{"cf":"ericcson","col":"sgsnchange","type":"string"},\
"diagnostics":{"cf":"ericcson","col":"diagnostics","type":"string"},\
"accesspointnameoi":{"cf":"ericcson","col":"accesspointnameoi","type":"string"},\
"cip_scfaddress":{"cf":"ericcson","col":"cip_scfaddress","type":"string"},\
"cip_servicekey":{"cf":"ericcson","col":"cip_servicekey","type":"string"},\
"cip_defaulttransactionhandling":{"cf":"ericcson","col":"cip_defaulttransactionhandling","type":"string"},\
"cip_camelaccesspointnameni":{"cf":"ericcson","col":"cip_camelaccesspointnameni","type":"string"},\
"cip_camelaccesspointnameoi":{"cf":"ericcson","col":"cip_camelaccesspointnameoi","type":"string"},\
"cip_numberofdpencountered":{"cf":"ericcson","col":"cip_numberofdpencountered","type":"string"},\
"cip_levelofcamelservice":{"cf":"ericcson","col":"cip_levelofcamelservice","type":"string"},\
"cip_freeformatdata":{"cf":"ericcson","col":"cip_freeformatdata","type":"string"},\
"cip_ffdappendindicator":{"cf":"ericcson","col":"cip_ffdappendindicator","type":"string"},\
"plmnidentifier":{"cf":"ericcson","col":"plmnidentifier","type":"string"},\
"matched":{"cf":"ericcson","col":"matched","type":"string"},\
"pgw_ipa_ipbinv4address":{"cf":"ericcson","col":"pgw_ipa_ipbinv4address","type":"string"},\
"pgw_ipa_ipbinv6address":{"cf":"ericcson","col":"pgw_ipa_ipbinv6address","type":"string"},\
"pgw_iptra_ipstringv4address":{"cf":"ericcson","col":"pgw_iptra_ipstringv4address","type":"string"},\
"pgw_iptra_ipstringv6address":{"cf":"ericcson","col":"pgw_iptra_ipstringv6address","type":"string"},\
"sgw_ipa_ipbinv4address":{"cf":"ericcson","col":"sgw_ipa_ipbinv4address","type":"string"},\
"sgw_ipa_ipbinv6address":{"cf":"ericcson","col":"sgw_ipa_ipbinv6address","type":"string"},\
"sgw_iptra_ipstringv4address":{"cf":"ericcson","col":"sgw_iptra_ipstringv4address","type":"string"},\
"sgw_iptra_ipstringv6address":{"cf":"ericcson","col":"sgw_iptra_ipstringv6address","type":"string"},\
"sna_ipa_ipbinv4address":{"cf":"ericcson","col":"sna_ipa_ipbinv4address","type":"string"},\
"sna_ipa_ipbinv6address":{"cf":"ericcson","col":"sna_ipa_ipbinv6address","type":"string"},\
"sna_iptra_ipstringv4address":{"cf":"ericcson","col":"sna_iptra_ipstringv4address","type":"string"},\
"sna_iptra_ipstringv6address":{"cf":"ericcson","col":"sna_iptra_ipstringv6address","type":"string"},\
"pdppdntype":{"cf":"ericcson","col":"pdppdntype","type":"string"},\
"spdppdna_ipa_ipba_ipbinv4addr":{"cf":"ericcson","col":"spdppdna_ipa_ipba_ipbinv4addr","type":"string"},\
"spdppdna_ipa_ipba_ipbinv6addr":{"cf":"ericcson","col":"spdppdna_ipa_ipba_ipbinv6addr","type":"string"},\
"spdppdna_ipa_iptra_iptxtv4addr":{"cf":"ericcson","col":"spdppdna_ipa_iptra_iptxtv4addr","type":"string"},\
"spdppdna_ipa_iptra_iptxtv6addr":{"cf":"ericcson","col":"spdppdna_ipa_iptra_iptxtv6addr","type":"string"},\
"spdppdna_etsiaddress":{"cf":"ericcson","col":"spdppdna_etsiaddress","type":"string"},\
"servingnodeplmnidentifier_mcc":{"cf":"ericcson","col":"servingnodeplmnidentifier_mcc","type":"string"},\
"servingnodeplmnidentifier_mnc":{"cf":"ericcson","col":"servingnodeplmnidentifier_mnc","type":"string"},\
"servingnodetype":{"cf":"ericcson","col":"servingnodetype","type":"string"},\
"p_gwplmnidentifier_mcc":{"cf":"ericcson","col":"p_gwplmnidentifier_mcc","type":"string"},\
"p_gwplmnidentifier_mnc":{"cf":"ericcson","col":"p_gwplmnidentifier_mnc","type":"string"},\
"p_gwau_ipba_ipbinv4address":{"cf":"ericcson","col":"p_gwau_ipba_ipbinv4address","type":"string"},\
"p_gwau_ipba_ipbinv6address":{"cf":"ericcson","col":"p_gwau_ipba_ipbinv6address","type":"string"},\
"p_gwau_iptra_ipstringv4address":{"cf":"ericcson","col":"p_gwau_iptra_ipstringv4address","type":"string"},\
"p_gwau_iptra_ipstringv6address":{"cf":"ericcson","col":"p_gwau_iptra_ipstringv6address","type":"string"},\
"starttime":{"cf":"ericcson","col":"starttime","type":"string"},\
"stoptime":{"cf":"ericcson","col":"stoptime","type":"string"},\
"pdnconnectionid":{"cf":"ericcson","col":"pdnconnectionid","type":"string"},\
"spdppdnae_ip_ipba_ipbinv4addr":{"cf":"ericcson","col":"spdppdnae_ip_ipba_ipbinv4addr","type":"string"},\
"spdppdnae_ip_ipba_ipbinv6addr":{"cf":"ericcson","col":"spdppdnae_ip_ipba_ipbinv6addr","type":"string"},\
"spdppdnae_ip_iptra_iptxtv4addr":{"cf":"ericcson","col":"spdppdnae_ip_iptra_iptxtv4addr","type":"string"},\
"spdppdnae_ip_iptra_iptxtv6addr":{"cf":"ericcson","col":"spdppdnae_ip_iptra_iptxtv6addr","type":"string"},\
"spdppdnaddressext_etsiaddress":{"cf":"ericcson","col":"spdppdnaddressext_etsiaddress","type":"string"},\
"sgwchange":{"cf":"ericcson","col":"sgwchange","type":"string"},\
"originalfile":{"cf":"ericcson","col":"originalfile","type":"string"},\
"recordextensions_information":{"cf":"ericcson","col":"recordextensions_information","type":"string"},\
"losd_chargingrulebasename":{"cf":"ericcson","col":"losd_chargingrulebasename","type":"string"},\
"losd_timequotamechanism":{"cf":"ericcson","col":"losd_timequotamechanism","type":"string"},\
"dynamicaddressflagext":{"cf":"ericcson","col":"dynamicaddressflagext","type":"string"},\
"fabricante":{"cf":"ericcson","col":"fabricante","type":"string"},\
"recordopeningdate":{"cf":"ericcson","col":"recordopeningdate","type":"string"},\
"elementorede":{"cf":"ericcson","col":"elementorede","type":"string"},\
"tecnologia":{"cf":"ericcson","col":"tecnologia","type":"string"},\
"ipggsn":{"cf":"ericcson","col":"ipggsn","type":"string"},\
"ipsgsn":{"cf":"ericcson","col":"ipsgsn","type":"string"},\
"cgi":{"cf":"ericcson","col":"cgi","type":"string"},\
"tipo_assinante":{"cf":"ericcson","col":"tipo_assinante","type":"string"},\
"tipo_tarifacao":{"cf":"ericcson","col":"tipo_tarifacao","type":"string"},\
"volumedownlink":{"cf":"ericcson","col":"volumedownlink","type":"string"},\
"volumeuplink":{"cf":"ericcson","col":"volumeuplink","type":"string"},\
"tac":{"cf":"ericcson","col":"tac","type":"string"}}})

cat = json.dumps({"table":{"namespace":"default", "name":"tbl_users_affected_cnt_hb", "tablecoder":"primitivetype"},"rowkey":"rowkey","columns":{"rowkey":{"cf":"rowkey", "col":"rowkey","type":"string"},\
"accesspointnameni":{"cf":"ericcson1","col":"accesspointnameni","type":"string"},\
"causeforrecclosing":{"cf":"ericcson2","col":"causeforrecclosing","type":"string"},\
"cdr_reason":{"cf":"ericcson3","col":"cdr_reason","type":"string"},\
"duration":{"cf":"ericcson4","col":"duration","type":"string"},\
"recordopeningtime":{"cf":"ericcson5","col":"recordopeningtime","type":"string"},\
"servedimsi":{"cf":"ericcson6","col":"servedimsi","type":"string"},\
"terminated_count":{"cf":"ericcson7","col":"terminated_count","type":"string"}}})

cat_val = json.dumps({"table":{"namespace":"default", "name":"tbl_users_crossed_vollimit_hb", "tablecoder":"primitivetype"},"rowkey":"rowkey","columns":{"rowkey":{"cf":"rowkey", "col":"rowkey","type":"string"},\
"accesspointnameni":{"cf":"ericcson1","col":"accesspointnameni","type":"string"},\
"causeforrecclosing":{"cf":"ericcson2","col":"causeforrecclosing","type":"string"},\
"cdr_reason":{"cf":"ericcson3","col":"cdr_reason","type":"string"},\
"duration":{"cf":"ericcson4","col":"duration","type":"string"},\
"recordopeningtime":{"cf":"ericcson5","col":"recordopeningtime","type":"string"},\
"servedimsi":{"cf":"ericcson6","col":"servedimsi","type":"string"},\
"limit_crossed_cnt":{"cf":"ericcson7","col":"terminated_count","type":"string"}}})


df=sqlContext.read.option("catalog",cat_main).option("newtable","2").format("org.apache.spark.sql.execution.datasources.hbase").load()

df.registerTempTable("tim_ericcson_bulk")

df1=sqlContext.sql("SELECT rowkey,accesspointnameni,causeforrecclosing,duration,\
CONCAT(substring(recordopeningtime,1,4),'-',substring(recordopeningtime,5,2),'-',substring(recordopeningtime,7,2),' ','00:00:00.000') AS recordopeningtime,servedimei,servedimsi from tim_ericcson_bulk where causeforrecclosing='4'")

df1.registerTempTable("tim_ericcson_bulk1")

df1=sqlContext.sql("SELECT max(rowkey) rowkey,max(accesspointnameni) accesspointnameni,max(causeforrecclosing) causeforrecclosing,max(duration) duration,\
recordopeningtime,servedimsi,'Abnormal Termination' cdr_reason ,count(servedimsi) terminated_count \
from tim_ericcson_bulk1 \
where causeforrecclosing='4'\
group by servedimsi,recordopeningtime")

df1.registerTempTable("tim_ericcson_bulk2")

df2=sqlContext.sql("SELECT rowkey,accesspointnameni,causeforrecclosing,duration,recordopeningtime,servedimsi,cdr_reason,CAST(terminated_count AS STRING) terminated_count from tim_ericcson_bulk2")

##trial1="TBL_USERS_AFFECTED_CNT"

df11=sqlContext.sql("SELECT rowkey,causeforrecclosing,\
CONCAT(substring(recordopeningtime,1,4),'-',substring(recordopeningtime,5,2),'-',substring(recordopeningtime,7,2),' ','00:00:00.000') AS recordopeningtime,\
'Exceeded Volume Limit' cdr_reason ,servedimsi from tim_ericcson_bulk where causeforrecclosing='16'")

df11.registerTempTable("tim_ericcson_bulk11")

df12=sqlContext.sql("SELECT max(rowkey) rowkey,max(causeforrecclosing) causeforrecclosing,\
recordopeningtime,servedimsi,'Crossed volume Limit' cdr_reason ,count(servedimsi) limit_crossed_cnt \
from tim_ericcson_bulk11 \
where causeforrecclosing='16'\
group by servedimsi,recordopeningtime")

df12.registerTempTable("tim_ericcson_bulk22")

df21=sqlContext.sql("SELECT rowkey,causeforrecclosing,recordopeningtime,servedimsi,cdr_reason,CAST(limit_crossed_cnt AS STRING) limit_crossed_cnt from tim_ericcson_bulk22")

df21.show()

##trial1="TBL_USERS_CROSSED_VOLLIMIT"

try:    
    df21.write.option("catalog",cat_val).option("newtable","4").format("org.apache.spark.sql.execution.datasources.hbase").save()
except Exception as e:
   aa=2

try:
   df2.write.option("catalog",cat).option("newtable","4").format("org.apache.spark.sql.execution.datasources.hbase").save()
except Exception as e:
   aa=2
