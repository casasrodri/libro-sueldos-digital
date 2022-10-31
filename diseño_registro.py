DISEÑO1 = {
    'registro': 2,
    'cuit': 11,
    'envio': 2,
    'periodo': 6,
    'tipo_liquidacion': 1,
    'nro_liquidacion': 5,
    'dias_base': 2,
    'cant_trabajadores': 6
}

DISEÑO2 = {
    'registro': 2,
    'cuil': 11,
    'legajo': 10,
    'dependencia_revista': 50,
    'cbu': 22,
    'dias_prop_tope': 3,
    'fecha_pago': 8,
    'fecha_rubrica': 8,
    'forma_pago': 1
}

DISEÑO3 = {
    'registro': 2,
    'cuil': 11,
    'codigo_concepto_liquidado': 10,
    'cantidad': 5,
    'unidades': 1,
    'importe': 15,
    'debcre': 1,
    'periodo_retro': 6
}

DISEÑO4 = {
    'registro': 2,
    'cuil': 11,
    'conyuge': 1,
    'hijos': 2,
    'marca_cct': 1,
    'marca_scvo': 1,
    'marca_reduccion': 1,
    'tipo_empleador': 1,
    'tipo_operacion': 1,
    'sit_revista': 2,
    'condicion': 2,
    'actividad': 3,
    'modalidad_contratacion': 3,
    'siniestrado': 2,
    'localidad': 2,
    'sit_revista_1': 2,
    'sit_revista_1_dia': 2,
    'sit_revista_2': 2,
    'sit_revista_2_dia': 2,
    'sit_revista_3': 2,
    'sit_revista_3_dia': 2,
    'dias_trabajados': 2,
    'horas_trabajadas': 3,
    'porc_adic_seg_soc': 5,
    'porc_contrib_tarea_dif': 5,
    'obra_social': 6,
    'adherentes_obra_soc': 2,
    'aporte_adic_obra_soc': 15,
    'contrib_adic_obra_soc': 15,
    'base_aporte_obra_social_fsr': 15,
    'base_contrib_obra_social_fsr': 15,
    'base_diferencial_lrt': 15,
    'rem_maternidad_anses': 15,
    'bruto': 15,
    'base_imponible1': 15,
    'base_imponible2': 15,
    'base_imponible3': 15,
    'base_imponible4': 15,
    'base_imponible5': 15,
    'base_imponible6' : 15,
    'base_imponible7': 15,
    'base_imponible8': 15,
    'base_imponible9': 15,
    'base_dif_aporte_seg_soc': 15,
    'base_dif_contrib_seg_soc': 15,
    'base_imponible10': 15,
    'importe_detraer': 15
}

def leer_registro(linea):
    if linea.startswith('01'):
        diseño = DISEÑO1
    elif linea.startswith('02'):
        diseño = DISEÑO2
    elif linea.startswith('03'):
        diseño = DISEÑO3
    elif linea.startswith('04'):
        diseño = DISEÑO4
    else:
        print(linea)
        raise TypeError("Tipo de registro no aceptado (debe comenzar con 01 al 04).")

    out = {}
    aux = 0
    for campo, largo in diseño.items():
        out[campo] = linea[aux:aux+largo]
        aux = aux+largo

    return out

def dict_to_linea(diccionario):
    return ''.join(str(x) for x in diccionario.values())