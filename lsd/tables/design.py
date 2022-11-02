from tables.elements import *

DISEÑO1 = Tabla([
    Campo('registro',                       2,  TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('cuit',                           11, TIPO.NUM),
    Campo('envio',                          2,  TIPO.STR),
    Campo('periodo',                        6,  TIPO.NUM),
    Campo('tipo_liquidacion',               1,  TIPO.STR),
    Campo('nro_liquidacion',                5,  TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('dias_base',                      2,  TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('cant_trabajadores',              6,  TIPO.NUM, LADO.IZQ, RELLENO.CERO)
])

DISEÑO2 = Tabla([
    Campo('registro',                       2,  TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('cuil',                           11, TIPO.NUM),
    Campo('legajo',                         10, TIPO.STR, LADO.DER, RELLENO.ESPACIO),
    Campo('dependencia_revista',            50, TIPO.STR, LADO.DER, RELLENO.ESPACIO),
    Campo('cbu',                            22, TIPO.STR),
    Campo('dias_prop_tope',                 3,  TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('fecha_pago',                     8,  TIPO.DATE),
    Campo('fecha_rubrica',                  8,  TIPO.DATE, LADO.DER, RELLENO.ESPACIO),
    Campo('forma_pago',                     1,  TIPO.NUM)
])

DISEÑO3 = Tabla([
    Campo('registro',                       2,  TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('cuil',                           11, TIPO.NUM),
    Campo('codigo_concepto_liquidado',      10, TIPO.STR, LADO.DER, RELLENO.ESPACIO),
    Campo('cantidad',                       5,  TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('unidades',                       1,  TIPO.STR, LADO.IZQ, RELLENO.ESPACIO),
    Campo('importe',                        15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('debcre',                         1,  TIPO.STR),
    Campo('periodo_retro',                  6,  TIPO.DATE, LADO.DER, RELLENO.ESPACIO)
])

DISEÑO4 = Tabla([
    Campo('registro',                       2,  TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('cuil',                           11, TIPO.NUM),
    Campo('conyuge',                        1,  TIPO.BOOL),
    Campo('hijos',                          2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('marca_cct',                      1, TIPO.BOOL),
    Campo('marca_scvo',                     1, TIPO.BOOL),
    Campo('marca_reduccion',                1, TIPO.BOOL),
    Campo('tipo_empleador',                 1, TIPO.NUM),
    Campo('tipo_operacion',                 1, TIPO.NUM),
    Campo('sit_revista',                    2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('condicion',                      2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('actividad',                      3, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('modalidad_contratacion',         3, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('siniestrado',                    2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('localidad',                      2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('sit_revista_1',                  2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('sit_revista_1_dia',              2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('sit_revista_2',                  2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('sit_revista_2_dia',              2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('sit_revista_3',                  2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('sit_revista_3_dia',              2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('dias_trabajados',                2, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('horas_trabajadas',               3, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('porc_adic_seg_soc',              5, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('porc_contrib_tarea_dif',         5, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('obra_social',                    6, TIPO.STR),
    Campo('adherentes_obra_soc',            3, TIPO.NUM, LADO.IZQ, RELLENO.CERO),
    Campo('aporte_adic_obra_soc',           15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('contrib_adic_obra_soc',          15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_aporte_obra_social_fsr',    15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_contrib_obra_social_fsr',   15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_diferencial_lrt',           15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('rem_maternidad_anses',           15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('bruto',                          15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible1',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible2',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible3',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible4',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible5',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible6',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible7',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible8',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible9',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_dif_aporte_seg_soc',        15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_dif_contrib_seg_soc',       15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('base_imponible10',               15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO),
    Campo('importe_detraer',                15, TIPO.FLOAT, LADO.IZQ, RELLENO.CERO) 
])