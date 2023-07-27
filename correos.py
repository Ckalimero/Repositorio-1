import re

# La lista de correos electrónicos que proporcionaste
emails = """
... luis.abeytua.p@gmail.com,info@famavigo.com, FERNANDOABREU60@GMAIL.COM,Adri.acevedo@gmail.com,povedaag1998@gmail.com,MPALBAMEDINA@HOTMAIL.COM,REGALA-MANITA_MHG@HOTMAIL.COM,vlopezcollado@gmail.com,javier.alihernandez@gmail.com,el.fran@hotmail.es,carlosalmansa2@gmail.com,almarzaytabanera@yahoo.es,antonio@forsepriv.com,carlam_98@hotmail.es,dolocalzado.dcg@gmail.com/ EMAIL - ALMUURENA92@HOTMAIL.ES,elrelaxariumderebeca@hotmail.com,miriamalgi@hotmail.com,RAULEMP@GMAIL.COM,JUANSEVAS1571@GMAIL.COM,sergioap80@gmail.com,MFAMOROS@HOTMAIL.COM,crixtinafernandez@hotmail.com// anabel170910@gmail.com,mariaisabel.garcia@uclm.es,regala-up10@hotmail.com,anabelengomez35@gmail.com,rafanguita@hotmail.com,REGALA-LDORADOC@YAHOO.ES,coachinmaculada@gmail.com,anac.fisioterapeuta@gmail.com,mai_2608@hotmail.com,mrborja9@gmail.com,mas@tragsa.es,marcos.arroyo.carrasco@gmail.com,MIGUEL1961@HOTMAIL.ES,labellaazu@gmail.com,marianievesbarbacontreras@gmail.com,PREESCOLARELSOL@HOTMAIL.COM,garciaastillerosbarrajon@gmail.com,csierrams@live.com,viracenquel2011@gmail.com,collado_corrales@hotmail.com,eb.infocentro@gmail.com,pedro.blanco@festivaldemerida.es,LUPE.BOORQUES@UNIVERSIDADEUROPEA.ES,almudenadonoso65@gmail.com,rosamariagonzalezrincon@gmail.com,¡robistofano@gmail.com,jorgeru@msn.com,santi19-62@hotmail.com ,jorgemillancabrera@gmail.com,palomacarretero@hotmail.com,sergio.sqll@outlook.com ,pololo_fiesta@hotmail.com, mhervas@sescam.org,vicentediaz_3@hotmail.com, torrespareja@gmail.com,celia_sanchezsobrino@hotmail.com,olgabustos@Gmail.com,tatis885@hotmail.com,raquelcajides@icloud.com,uno22uno@hotmail.com,alicamper@hotmail.com,piscinator@hotmail.com,elenacapilla@hotmail.com ,ccarballoaguilar@gmail.com,GCARRERAPE@GMAIL.COM,REDONDOHECTOR@GMAIL.COM,scasero_perez@hotmail.com,LIMONCALLERAS53@GMAIL.COM,letivalde@hotmail.com,mgema333@gmail.com//clienta:nininhaesbrasil@gmail.com,MARGAS.BENAYAS@HOTMAIL.COM,zoecg@gmail.com,m.rocio92@hotmail.com,JMCODEJON@GMAIL.COM,ocortijo@infonegocio.com,VICTOR.CRIADO2@GMAIL.COM,daniolmo3@hotmail.com,eljdav@gmail.com,nereadeenciso9@gmail.com ,ANTONIOYNURIA@HOTMAIL.ES,angelrbalmagro1@gmail.com ,PHERAS2512@GMAIL.COM,SANTAPAZGOMEZ@GMAIL.COM,MANITA_MHG@HOTMAIL.COM, ahoyog@gmail.com,nuriadelgadomunoz@gmail.com,Domingomarredo@gmail.com,sara_d_m@hotmail.com,anadomcej@gmail.com,luped63@gmail.com,claudia.dupuydelome@gmail.com,IGNACIOELGUERO@HOTMAIL.COM,terechu@movistar.es,JOSE@ENCINAS.EMAIL,AZAHARAFREUD@GMAIL.COM,pabloespla@gmail.com,export@espeltviticultors.com,mirellapr8@gmail.com,adrian.feliu@hotmail.com ,rmfernandezaranda@gmail.com,antoniofbarral@yahoo.es,ESFEES1@HOTMAIL.COM,maria.fernandezgallego4@gmail.com,MARINAFGARAY@GMAIL.COM,mfgomez21@gmail.com,varof97@gmail.com,dani50fernandezrubio@gmail.com,aurelie.ferraton@orange.fr,albertofitoab@gmail.com,celia.flores.cuenca@gmail.com,martafloresmartin@hotmail.com,logitamakatu@gmail.com,estebanj.hernandez@gmail.com,friaslopez@hotmail.es,CF@CARMENFCOMUNICACION.COM,arantxa@plumarestaurant.co.uk,aidafernandez_89@hotmail.com,andresgarcia2995@gmail.com,fcomechas@gmail.com,ANA.GAFRANC@GMAIL.COM,alicia@asesoresmg.com,pacogarcia@bodegasoran.com, cgvazquez1@gmail.com 
,pikatoste74@hotmail.com//,martagijon19@gmail.com,susanag1971@hotmail.com,anagg1982@hotmail.com,lorenamohedas@hotmail.com,franciscojaviergomezrubio@gmail.com,lorenzo.cg28@gmail.com,conchaypatrimonio@gmail.com,nataliag.s@hotmail.com,BEGOMEZVAL@gmail.com,mamencoronado@hotmail.com,TONIPER.66@GMAIL.COM,emiliano_balonmano@hotmail.com,regala-julianos72@yahoo.es ,antonio66683@gmail.com ,vgueb1974@hotmail.com,jaschezcarne@gmail.com,guillenvazquezsalvador@gmail.com,sergiogutierrezperez782@gmail.com,paco_bolsasypapel@hotmail.com,silvialoro@live.com ,chusfer102@gmail.com,jesusguzman22@hotmail.com,marcd66600@gmail.com,conchita_fernando@hotmail.com,focopssl@gmail.com,rememedinagracia@gmail.com,brahid2001@yahoo.es,jagonzalez@bankinter.com   / jmhurtadorama@gmail.com ,miguelangelgonzalezalmansa@gmail.com,ivanmartinezturrillo@gmail.com,gertjan@secon.es,regala-josecb600@hotmail.com,osquitar17.or@gmail.com,mgbar04@hotmail.com,gabrie_8@hotmail.com,aranchajimenezh@gmail.com,REGALA-SONIA.MOLINA9051@GMAIL.COM,chocajcc@gmail.com,BSQ.ECG@GMAIL.COM,JUANSOYYO_777@HOTMAIL.COM,maria_lago@yahoo.es,jaller72.alh@gmail.com,volemos_lejos@hotmail.com,ramon@ifsu.org,javier.lobo.zamarro@gmail.com,2960@icagr.es,ALOPEZLUCENDo@YAHOO.ES ,ferminlopeznevado@hotmail.com,VMLOPEZ@ADIF.ES,manuel.lopez.vidal@gmail.com,paquilorente@gmail.com,paquilorente@gmail.com,mjose407@hotmail.com,lozanoarias91@gmail.com,ferydori@gmail.com,isracasa@hotmail.com,m_maria0@hotmail.com,javiermajanovos@gmail.com ,anamalagoncabezas@gmail.com,CARLOTAMALDONADO@YAHOO.ES,mdolores27@outlook.es,secunpm@hotmail.com,prietoaldarias@yahoo.es,samuel-diaz89@hotmail.com,prado_sanchez_ruiz@hotmail.com,REGALA-MARIA2PAREJOGON@GMAIL.COM,valengopim@hotmail.com,luciacp_5@hotmail.com//,silvia_va_3@hotmail.com,bolshoi44@gmail.com,joselurubio@gmail.com,miguelmartinmac@gmail.com,beatrizlez@gmail.com,martinromerojp@hotmail.com,desi_martinez_12@hotmail.com,psicomarielamr@gmail.com,condes_12@hotmail.com ,ji.medinacrespo@gmail.com,jmeracandilejas@gmail.com,jcmerinor@gmail.com,TABARCA99@GMAIL.COM,silvia.millan.garcia.2002@hotmail.com,ANAMINGOTEV@GMAIL.COM,paolaa_86@hotmail.com,161raquel138@gmail.com,amoraperez3@gmail.com,adelasegurac60@gmail.com,carlos@castelldelremei.com,C.MORAGACUBAS@GMAIL.COM,JOSE.MORENO@GMAIL.COM,rosama82m@gmail.com,ropimo82@hotmail.com ,PRUDENMORENOARRONESGONZALEZ@GMAIL.COM,LUISMORENO.AU3D@GMAIL.COM,ANABELEN25_28@HOTMAIL.COM,zoskipor1@gmail.com,blancamoyo@hotmail.com,mcnieto2008@gmail.com,RAFAESTANCO7@GMAIL.COM,olilandt@gmail.com,ROSAJAVI0806@GMAIL.COM,zorroplateadomor@gmail.com,silvialoro@live.com,manolopalacios7@gmail.com,MAPAZ49.MP@GMAIL.COM ,nitacris12@gmail.com,rapeal65@gmail.com,fteamperez@gmail.com,HABIB_PE@HOTMAIL.COM,bernardo_tista@hotmail.com,carmen.tresc@gmail.com,castrodecordoba@hotmail.com,fany.prieto@gmail.com,inmaruizmestanza@gmail.com,JOSUE_ALTEC@HOTMAIL.COM,comercialrazvan@gmaikl.com,IRAINEROR@GMAIL.COM,jesusramirez74@hotmail.com,javierramirezsanz@hotmail.com ,mariasobrino21@gmail.com,scirocco82@hotmail.com,villaman-sl@hotmail.com,jv.regolf@hotmail.com,elis_rp@hotmail.com,Yuleisirijoromero1234@gmail.com,vrivas_san5@hotmail.com,AROcAMAS@HOTMAIL.COM,sirifis@hotmail.com,arodriguez@aguared.es,beatrizchaple@gmail.com,anadelmarmf@gmail.com,mariguadachavarria@hotmail.com,LOURDESRODRIGUEZ70@GMAIL.COM,carlosss919@gmail.com,julio12082@hotmail.com,RODRIGUEZSACRISTANM@GMAIL.COM,patrunbury@gmail.com,zahirar22@gmail.com,jcroncero@outlook.es,JOAQUIM@IMAGINAIMATGE.COM,valero11luis@gmail.com,arastruga@yahoo.es,morris_somarro@hotmail.com,sruizcosano@gmail.com,antonioluisruizh@gmail.com,NATARULO@GMAIL.COM,cruzsacedon@gmail.com,jsaiza@gmail.com,aliciasalabert@gmail.com,ana.salmeron.sanchez87@gmail.com,jesussanroman@gmail.com,frodobeefcake@gmail.com,itx.zuri@gmail.com ,anaisabel_serracarras@hotmail.com,rosa.sanchezsaez45@gmail.com,sergiosanchez@gmail.com,sonisr1974@gmail.com,estherydani2011@hotmail.com,INFO@CELLERCALPLA.COM,LCSANTISIMO@YAHOO.ES,nefer_silen@hotmail.com,vserranoaguilar@gmail.com/ clienta serranoaguilarbeatriz@gmail.com,serrano.anamon@gmail.com,VJSERRANORAMIREZ@HOTMAIL.COM,angelrbalmagro1@gmial.com,manuelcalas@hotmail.es,carmensp212001@gmail.com,csm1604.carmen@gmail.com,jesussotos91jesus@gmail.com,artursta24@protonmail.com,SUAREZPILAR@GMAIL.COM,jr.tajuelodiesma@gmail.com,aaronartstattoo@gmail.com,alvarotato@gmail.com,CHAROTEJERO25@GMAIL.COM,carpinteria.antonio@gmail.com,tiernesan@gmail.com,maria89_sanse@hotmail.com ,feryele@hotmail.com,chematudela@gmail.com,JUVEDAMORA@HOTMAIL.ES,rosa.lucia.valencia@gmail.com ,LAENCOMIENDARESTAURANTE@GMAIL.COM,Noviembrecompaniadeteatro@gmail.com, eduardovasco@yahoo.es,rossimarivasquez@gmail.com,loyolamartinfraiz@gmail.com,romerorpi@gmail.com- clienta-vergarsan@hotmail.com,NVIDAL@HORTITEC.ES,rosa.anlo@hotmail.com, mary-vh@live.com,ALVAROVILLENA84@GMAIL.COM,emilia@emiliayague.com,miguel.zarza@gmail.com
] ...
"""

# Expresión regular para identificar correos electrónicos válidos
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Filtrar y limpiar la lista de correos electrónicos
valid_emails = re.findall(email_pattern, emails)

# Convertir la lista filtrada en una cadena de texto con cada correo separado por comas
filtered_emails_str = ', '.join(valid_emails)

# Imprimir la lista de correos electrónicos limpiada
print(filtered_emails_str)