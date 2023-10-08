def get_register_from_line(
    line: str
    ) -> list:
    """This function creates a register to save in a pandas 
    dataframe in order to the glossary of Estructura Rol Cobro
    files.
    Parameters: 
    
    line (str): raw data from text file
    
    Returns:
    data (dict): dictionary with the structured data
    """
    assert(len(line)==117)
    
    comuna_actual = line[0:5]
    assert(len(comuna_actual)==5)
    year = line[5:9]
    assert(len(year)==4)
    semestre = line[9]
    assert(len(semestre)==1)
    indicador_de_aseo = line[10]
    assert(len(indicador_de_aseo)==1)
    espacios = line[11:17]
    assert(len(espacios)==6)
    direccion_predial = line[17:57]
    assert(len(direccion_predial)==40)
    manzana_actual = line[57:62]
    assert(len(manzana_actual)==5)
    predio_actual = line[62:67]
    assert(len(predio_actual)==5)
    codigo_de_serie = line[67]
    assert(len(codigo_de_serie)==1)
    cuota_trimestral = line[68:81]
    assert(len(cuota_trimestral)==13)
    avaluo_total = line[81:96]
    assert(len(avaluo_total)==15)
    avaluo_exento = line[96:111]
    assert(len(avaluo_exento)==15) 
    year_termino_exencion = line[111:115]
    assert(len(year_termino_exencion)==4)
    codigo_ubicacion = line[115]
    assert(len(codigo_ubicacion)==1)
    codigo_destino = line[116]
    assert(len(codigo_destino)==1)
    
    data = [int(comuna_actual), int(year), int(semestre), indicador_de_aseo, 
            direccion_predial, int(manzana_actual), int(predio_actual), 
            codigo_de_serie, int(cuota_trimestral), int(avaluo_total),
            int(avaluo_exento) , int(year_termino_exencion), codigo_ubicacion,
            codigo_destino]
    assert(len(data)==14)
    
    return data

def get_register_from_line_custom(
    line: str
    ) -> list:
    """This function creates a register to save in a pandas 
    dataframe in order to the glossary of Estructura Rol Cobro
    files.
    Parameters: 
    
    line (str): raw data from text file
    
    Returns:
    data (dict): dictionary with the structured data
    """
    assert(len(line)==117)
    
    comuna_actual = line[0:5]
    assert(len(comuna_actual)==5)
    year = line[5:9]
    assert(len(year)==4)
    semestre = line[9]
    assert(len(semestre)==1)
    indicador_de_aseo = line[10]
    assert(len(indicador_de_aseo)==1)
    espacios = line[11:17]
    assert(len(espacios)==6)
    direccion_predial = line[17:57]
    assert(len(direccion_predial)==40)
    manzana_actual = line[57:62]
    assert(len(manzana_actual)==5)
    predio_actual = line[62:67]
    assert(len(predio_actual)==5)
    codigo_de_serie = line[67]
    assert(len(codigo_de_serie)==1)
    cuota_trimestral = line[68:81]
    assert(len(cuota_trimestral)==13)
    avaluo_total = line[81:96]
    assert(len(avaluo_total)==15)
    avaluo_exento = line[96:111]
    assert(len(avaluo_exento)==15) 
    year_termino_exencion = line[111:115]
    assert(len(year_termino_exencion)==4)
    codigo_ubicacion = line[115]
    assert(len(codigo_ubicacion)==1)
    codigo_destino = line[116]
    assert(len(codigo_destino)==1)
    
    data = [int(comuna_actual), int(year), int(semestre), indicador_de_aseo, 
            #direccion_predial, int(manzana_actual), int(predio_actual), 
            codigo_de_serie, int(cuota_trimestral), int(avaluo_total),
            int(avaluo_exento) , #int(year_termino_exencion), 
            codigo_ubicacion,
            codigo_destino]
    #assert(len(data)==14)
    return data

mapper = {
    "Unnamed: 0": 'Codigo',
    "Unnamed: 1": 'Municipio',
    "IADM83 (M$) Casinos de Juegos Ley Nº19.995.": 'IADM83',
    "IADM97 (M$) Derechos de Aseo ": 'IADM97',
    "IADM98 (M$) Derechos de Aseo Cobro Directo y de Patentes Comerciales": 'IADM98',
    "IADM99 (M$) Derechos de Aseo por Impuesto Territorial": 'IADM99',
    "IADM10 (TAS) Disponibilidad Presupuestaria Municipal por Habitante (M$)": 'IADM10',
    "IADM140 (M$) Impuesto Territorial de Beneficio Municipal (Art. 37 DL 3063) ": 'IADM140',
    "IADM01 (M$) Ingresos Municipales (Ingreso Total Percibido)": 'IADM01',
    "IADM999 (M$) Ingresos Municipales (Ingreso Total Percibido) sin Saldo Inicial de Caja": 'IADM999',
    "IADM40 (M$) Ingresos por Fondo Común Municipal": 'IADM40',
    "IADM44 (M$) Ingresos por Impuestos": 'IADM44',
    "IADM121 (M$) Ingresos por Patentes Municipales de Beneficio Municipal ": 'IADM121',
    "IADM122 (M$) Ingresos por Permisos de Circulación de Beneficio Municipal": 'IADM122',
    "IADM43 (M$) Ingresos por Transferencias": 'IADM43',
    "IADM43.1 (M$) Ingresos por Transferencias menos Casino Ley N° 19.995, Patentes Acuícolas y Patentes Mineras": 'IADM43.1',
    "IADM42 (M$) Ingresos Propios (IPP y FCM)": 'IADM42',
    "IADM41 (M$) Ingresos Propios Permanentes (IPP)": 'IADM41',
    "IADM74 (M$) Ingresos Propios Permanentes per Cápita (IPPP)": 'IADM74',
    "IADM49 (M$) Ingresos Propios, según criterio de Contraloría General de la República": 'IADM49',
    "IADM46 (M$) Ingresos Totales, descontados los Ingresos por Transferencias": 'IADM46',
    "IADM96 (M$) Monto Patentes Municipales Pagadas": 'IADM96',
    "IADM84 (M$) Patentes Acuícolas Ley Nº20.033 Art. 8.": 'IADM84',
    "IADM82 (M$) Patentes Mineras Ley Nº19.143.": 'IADM82',
    "IADM51 (M$) Gastos Corrientes": 'IADM51',
    "IADM85 (M$) Gastos en Bienes y Servicios de Consumo (Subtítulo 22)": 'IADM85',
    "IADM11 (M$) Gastos Municipales (Gastos Total Devengado)": 'IADM11',
    "BGMAAMUN (M$) Gastos Municipales Área de Gestión: Actividades Municipales": 'BGMAAMUN',
    "BGMAGINT (M$) Gastos Municipales Área de Gestión: Interna": 'BGMAGINT',
    "BGMAPCUL (M$) Gastos Municipales Área de Gestión: Programas Culturales": 'BGMAPCUL',
    "BGMAPREC (M$) Gastos Municipales Área de Gestión: Programas Recreacionales": 'BGMAPREC',
    "BGMAPSOC (M$) Gastos Municipales Área de Gestión: Programas Sociales": 'BGMAPSOC',
    "BGMASCOM (M$) Gastos Municipales Área de Gestión: Servicios Comunitarios": 'BGMASCOM',
    "IADM72.1 (M$) Gastos por Comisiones y Representaciones del Municipio": 'IADM72.1',
    "IADM39 (M$) Monto Transferido al Fondo Común Municipal": 'IADM39',
    "IADM72 (M$) Viáticos Personal de Planta y Contrata": 'IADM72',
}

mapper_2 = {'Unnamed: 0': 'Codigo', 
            'Unnamed: 1': 'Municipio', 
            'IADM97 (M$) Derechos de Aseo ':'IDA',
            'IADM99 (M$) Derechos de Aseo por Impuesto Territorial':'IDAxIT',
            'IADM140 (M$) Impuesto Territorial de Beneficio Municipal (Art. 37 DL 3063) ':'IT',
            'IADM41 (M$) Ingresos Propios Permanentes (IPP)':'IPP',
            'BSASC (M$) Servicios de Aseo y Recolección de Basura a la Comunidad.':'GDA',
           }

mapper_3 ={'Unnamed: 0': 'Codigo',
           'Unnamed: 1': 'Municipio',
           'IADM97 (M$) Derechos de Aseo ': 'IDA',
           'IADM98 (M$) Derechos de Aseo Cobro Directo y de Patentes Comerciales': 'IDAxCDyPC',
           'IADM99 (M$) Derechos de Aseo por Impuesto Territorial':'IDAxIT',
           'IADM140 (M$) Impuesto Territorial de Beneficio Municipal (Art. 37 DL 3063) ':'IT',
           'IADM40 (M$) Ingresos por Fondo Común Municipal':'IFCM',
           'IADM42 (M$) Ingresos Propios (IPP y FCM)':'IP',
           'IADM41 (M$) Ingresos Propios Permanentes (IPP)':'IPP',
           'IADM51 (M$) Gastos Corrientes':'GC',
           'IADM85 (M$) Gastos en Bienes y Servicios de Consumo (Subtítulo 22)':'GBySC',
           'IADM11 (M$) Gastos Municipales (Gastos Total Devengado)':'GT',
           'BGMASCOM (M$) Gastos Municipales Área de Gestión: Servicios Comunitarios':'GSC',
           'IADM39 (M$) Monto Transferido al Fondo Común Municipal':'GFCM',
           'IADM61 (M$) Gastos en Personal Municipal (Subtítulo 21)':'GP',
           'IADM91 (M$) Consumo de Agua':'CA',
           'BGASC (M$) Consumo de Agua en Servicios Comunitarios.':'CASC',
           'IADM90 (M$) Consumo de Electricidad':'CE',
           'BGESC (M$) Consumo de Electricidad en Servicios Comunitarios.':'CESC',
           'IADM92 (M$) Servicios de Aseo, Recolección de Basura y Vertederos':'DAyV',
           'BSASC (M$) Servicios de Aseo y Recolección de Basura a la Comunidad.':'DAC',
           'IADM93 (M$) Servicios de Mantención de Alumbrado Público':'GAP',
           'BSMJSC (M$) Servicios de Mantención de Jardines de la Comunidad.':'GJC',
           'BSMJGI (M$) Servicios de Mantención de Jardines Dependencias Municipales.':'GJDM',
           'IADM120 (M$) Servicios de Mantención de Jardines Total Gastos devengados':'GJ',
           'IADM95 (M$) Servicios de Mantención de Señalización de Tránsito':'GST',
           'IADM94 (M$) Servicios de Mantención de Semáforos':'GS',
           'FCM001 (M$) Monto Percibido por Fondo Común Municipal (FCM) al 31 de Diciembre, transferido por TGR (corresponde al monto total percibido por Anticipos Pagados, Saldos Pagados y Aporte Fiscal Pagado).':'TFCM'
    
}

region_dict = {'01': 'Tarapacá',
               '02': 'Antofagasta',
               '03': 'Atacama',
               '04': 'Coquimbo',
               '05': 'Valparaíso',
               '06': "O'Higgins",
               '07': 'Maule',
               '08': 'Bío-Bío',
               '09': 'Araucanía',
               '10': 'Los Lagos',
               '11': 'Aysén',
               '12': 'Magallanes',
               '13': 'Metropolitana',
               '14': 'Los Ríos',
               '15': 'Arica y Parinacota',
               '16': 'Ñuble'
               }

def check_data(df1, df2, df3):
    filas, columnas = False, False

    if (df1.columns == df2.columns).all() and (df2.columns == df3.columns).all():
        print("Las columnas coinciden")
        columnas = True
    else:
        print("ERROR: las columnas no coinciden. Revisar con excel")

    if (len(df1) == len(df2))  and (len(df2) == len(df3)):
        print("Las filas coinciden")
        filas = True
    else:
        print("ERROR: las filas no coinciden. Revisar con excel")   

    if filas and columnas:
        print("")
        print("Todo OK. Seguimos")