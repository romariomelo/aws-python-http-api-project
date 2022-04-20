def extract_info(pdf_file, palavras):
    """Processo"""
    primeiraLetraProcesso = pdf_file.find("P")
    processo = pdf_file[primeiraLetraProcesso+10:primeiraLetraProcesso+30]

    """Interessado"""
    interessado_inicio = pdf_file.find("INTERESSAD")
    interessado_final = pdf_file.find("RELATOR")
    interesado = pdf_file[interessado_inicio:interessado_final]


    """Relator"""
    relator_inicio = pdf_file.find("RELATOR")
    relator_final = pdf_file.find("RESPONSÁVEL:")
    relator = pdf_file[relator_inicio:relator_final]
  

    """RESPONSÁVEL"""
    responsavel_inicio = pdf_file.find("RESPONSÁVEL:")
    responsavel_final = pdf_file.find("ASSUNTO:")
    responsavel = pdf_file[responsavel_inicio:responsavel_final]

    """Assunto"""
    assunto_inicio = pdf_file.find("ASSUNTO:")
    assunto_final = pdf_file.find("I – RELATÓRIO")
    assunto= pdf_file[assunto_inicio:assunto_final]

    """ Relatório """
    relatorio_inicio = pdf_file.find("– RELATÓRIO")
    relatorio_final = pdf_file.find("II – FUNDAMENTAÇÃO")
    relatorio = pdf_file[relatorio_inicio+12:relatorio_final]

    """ Fundamentação """
    fundamentacao_inicio = pdf_file.find("II – FUNDAMENTAÇÃO")
    fundamentacao_final = pdf_file.find("III – DIREITO")
    fundamentacao = pdf_file[fundamentacao_inicio+18:fundamentacao_final]

    """Direito"""
    direito_inicio = pdf_file.find("III – DIREITO")
    direito_final = pdf_file.find("IV – DISPOSITIVO")
    direito = pdf_file[direito_inicio+14:direito_final]
   
    """Dispositivo"""
    dispositivo_inicio = pdf_file.find("– DISPOSITIVO")
    dispositivo_final = pdf_file.find("Brasília,")
    dispositivo = pdf_file[dispositivo_inicio+14:dispositivo_final]

    """Data"""
    data = pdf_file[dispositivo_final:-1]
    data_final = data.find(".")
    dt = data[10:data_final]

    response = {
        "processo": processo,
        "interessado": interesado,
        "relator": relator,
        "responsavel": responsavel,
        "assunto": assunto,
        "dispositivo": dispositivo,
        "data": dt,
        "palavras": palavras,
        "relatorio": relatorio,
        "fundamentacao": fundamentacao,
        "direito": direito,
    }

    return response
