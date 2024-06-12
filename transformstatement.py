from pandas import DataFrame


def transform_statement(document):
    keys = ["FECHA", "REFERENCIA", "NRO", "DEBITO", "CREDITO", "SALDO", "DETALLE"]

    my_dict = {key: [] for key in keys}
    net_lines = []
    for i in range(len(document)):
        page = document.load_page(i)
        text = page.get_text()
        net_lines.extend(text[text.find("FECHA") :].split("\n")[1:])
    fecha = ""
    for j_ in range(len(net_lines)):
        j = net_lines[j_]
        if j and j[1] != " ":
            fecha = j[:7]
        if j and j[9] == "-":
            my_dict["FECHA"].append(fecha.strip())
            my_dict["REFERENCIA"].append(j[10:33].strip())
            my_dict["NRO"].append(j[33:50].strip())
            my_dict["DEBITO"].append(j[50:70].strip())
            my_dict["CREDITO"].append(j[70:90].strip())
            my_dict["SALDO"].append(j[90:120].strip())
            detalle = ""
            for k in range(3):
                try:
                    if net_lines[j_ + k][9] != "-":
                        detalle += net_lines[j_ + k]
                except:
                    pass
            my_dict["DETALLE"].append(detalle)
        df = DataFrame(my_dict)

    return df.to_csv()
    
