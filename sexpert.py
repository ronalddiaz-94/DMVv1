from experta import *

#lista_sintomas=["nausea", "fiebre", "presion baja", "dolor cabeza"]
#lista_sintomas=["fiebre","dolor cabeza"]
lista_sintomas=[]
mapa_sintomas= {}

def creacionMapaSintomas():
  mapa_sintomas["['No','No','No','No','Si','No','No','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','No','Si','Si','No','Si','No','No','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si']"]= "Apendicitis"
  mapa_sintomas["['No','No','No','No','No','No','Si','No','No','No','No','No','No','Si','No','No','No','No','No','No','No','Si','No','No','Si','No','No','No','Si','No','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si']"]= "Colelitiasis"
  mapa_sintomas["['No','No','No','Si','No','Si','No','No','No','No','No','No','No','No','No','Si','No','No','No','Si','No','No','No','Si','Si','No','No','No','No','No','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','Si','Si']"]= "Neumonía"
  mapa_sintomas["['No','No','No','No','Si','No','No','No','No','No','No','Si','No','No','No','No','Si','No','No','No','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si']"]= "Gastroenteritis"
  mapa_sintomas["['No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','No','Si','No','No','Si','No','No']"]= "Asma"
  mapa_sintomas["['No','No','No','No','No','No','Si','No','No','Si','No','No','Si','No','No','No','No','No','No','Si','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','Si','Si','No','Si','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si']"]= "Infección renal"
  mapa_sintomas["['No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','No','No','No','No','No','Si','Si','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','No']"]= "Trastorno de ansiedad"
  mapa_sintomas["['No','No','No','No','No','No','No','No','Si','No','Si','No','No','No','No','No','No','No','No','No','No','Si','No','Si','Si','No','Si','No','Si','No','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si']"]= "Hepatitis"
  mapa_sintomas["['Si','Si','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','No','No','No','No','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','Si','No','No','Si','No','No','No','No','No','No']"]= "Hipotiroidismo"
  mapa_sintomas["['No','Si','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','No','No','No','No','No','No','No','Si','No','No','No','Si','No','No','No','Si','No','No','No','No','Si','Si','No','No','Si','No','No','No','No']"]= "Hipertiroidismo"
  mapa_sintomas["['No','No','No','No','No','No','No','No','No','No','No','Si','No','No','Si','No','No','No','Si','No','No','No','No','No','No','No','No','No','No','No','No','Si','No','Si','No','No','No','No','No','Si','No','Si','No','No','No','No','No','No','No','No','No','Si','No','No']"]= "Sinusitis"


class diagnostico(KnowledgeEngine):
  @DefFacts()
  def _initial_action(self):
    self.enf=""
    self.confianza=""
    yield Fact(action="Buscando enfermedad")

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Aum_Pes=W())), salience=1)
  def sintoma1(self):
    self.declare(Fact(Aum_Pes="Si")) if "Aumento de peso" in lista_sintomas else self.declare(Fact(Aum_Pes="No"))


  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Deb_Mus=W())), salience=1)
  def sintoma2(self):
    self.declare(Fact(Deb_Mus="Si")) if "Debilidad muscular" in lista_sintomas else self.declare(Fact(Deb_Mus="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dep=W())), salience=1)
  def sintoma3(self):
    self.declare(Fact(Dep="Si")) if "Depresión" in lista_sintomas else self.declare(Fact(Dep="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Desor=W())), salience=1)
  def sintoma4(self):
    self.declare(Fact(Desor="Si")) if "Desorientación" in lista_sintomas else self.declare(Fact(Desor="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Diarr=W())), salience=1)
  def sintoma5(self):
    self.declare(Fact(Diarr="Si")) if "Diarrea" in lista_sintomas else self.declare(Fact(Diarr="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dif_res=W())), salience=1)
  def sintoma6(self):
    self.declare(Fact(Dif_res="Si")) if "Dificultad para respirar" in lista_sintomas else self.declare(Fact(Dif_res="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Abd=W())), salience=1)
  def sintoma7(self):
    self.declare(Fact(Dol_Abd="Si")) if "Dolor Abdominal" in lista_sintomas else self.declare(Fact(Dol_Abd="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Abd_inf=W())), salience=1)
  def sintoma8(self):
    self.declare(Fact(Dol_Abd_inf="Si")) if "Dolor Abdominal Inferior" in lista_sintomas else self.declare(Fact(Dol_Abd_inf="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Abd_sup=W())), salience=1)
  def sintoma9(self):
    self.declare(Fact(Dol_Abd_sup="Si")) if "Dolor abdominal superior" in lista_sintomas else self.declare(Fact(Dol_Abd_sup="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Ori=W())), salience=1)
  def sintoma10(self):
    self.declare(Fact(Dol_Ori="Si")) if "Dolor al orinar" in lista_sintomas else self.declare(Fact(Dol_Ori="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Art=W())), salience=1)
  def sintoma11(self):
    self.declare(Fact(Dol_Art="Si")) if "Dolor articular" in lista_sintomas else self.declare(Fact(Dol_Art="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Cab=W())), salience=1)
  def sintoma12(self):
    self.declare(Fact(Dol_Cab="Si")) if "Dolor de cabeza" in lista_sintomas else self.declare(Fact(Dol_Cab="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Esp=W())), salience=1)
  def sintoma13(self):
    self.declare(Fact(Dol_Esp="Si")) if "Dolor de espalda" in lista_sintomas else self.declare(Fact(Dol_Esp="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Hom=W())), salience=1)
  def sintoma14(self):
    self.declare(Fact(Dol_Hom="Si")) if "Dolor de hombros" in lista_sintomas else self.declare(Fact(Dol_Hom="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Oid=W())), salience=1)
  def sintoma15(self):
    self.declare(Fact(Dol_Oid="Si")) if "Dolor de oído" in lista_sintomas else self.declare(Fact(Dol_Oid="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Pec=W())), salience=1)
  def sintoma16(self):
    self.declare(Fact(Dol_Pec="Si")) if "Dolor de pecho al respirar" in lista_sintomas else self.declare(Fact(Dol_Pec="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Est=W())), salience=1)
  def sintoma17(self):
    self.declare(Fact(Dol_Est="Si")) if "Dolor estomacal" in lista_sintomas else self.declare(Fact(Dol_Est="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Mus=W())), salience=1)
  def sintoma18(self):
    self.declare(Fact(Dol_Mus="Si")) if "Dolor muscular" in lista_sintomas else self.declare(Fact(Dol_Mus="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Dol_Car=W())), salience=1)
  def sintoma19(self):
    self.declare(Fact(Dol_Car="Si")) if "Dolor o presion en cara" in lista_sintomas else self.declare(Fact(Dol_Car="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Escal=W())), salience=1)
  def sintoma20(self):
    self.declare(Fact(Escal="Si")) if "Escalofríos" in lista_sintomas else self.declare(Fact(Escal="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Falt_Air=W())), salience=1)
  def sintoma21(self):
    self.declare(Fact(Falt_Air="Si")) if "Falta de aire" in lista_sintomas else self.declare(Fact(Falt_Air="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Falt_Ape=W())), salience=1)
  def sintoma22(self):
    self.declare(Fact(Falt_Ape="Si")) if "Falta de apetito" in lista_sintomas else self.declare(Fact(Falt_Ape="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Falt_Con=W())), salience=1)
  def sintoma23(self):
    self.declare(Fact(Falt_Con="Si")) if "Falta de concentracion" in lista_sintomas else self.declare(Fact(Falt_Con="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Fatig=W())), salience=1)
  def sintoma24(self):
    self.declare(Fact(Fatig="Si")) if "Fatiga" in lista_sintomas else self.declare(Fact(Fatig="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Fieb=W())), salience=1)
  def sintoma25(self):
    self.declare(Fact(Fieb="Si")) if "Fiebre" in lista_sintomas else self.declare(Fact(Fieb="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Flatu=W())), salience=1)
  def sintoma26(self):
    self.declare(Fact(Flatu="Si")) if "Flatulencia" in lista_sintomas else self.declare(Fact(Flatu="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Hec_Col=W())), salience=1)
  def sintoma27(self):
    self.declare(Fact(Hec_Col="Si")) if "Heces de color arcilla o gris" in lista_sintomas else self.declare(Fact(Hec_Col="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Hinc_Abd=W())), salience=1)
  def sintoma28(self):
    self.declare(Fact(Hinc_Abd="Si")) if "Hinchazón Abdominal" in lista_sintomas else self.declare(Fact(Hinc_Abd="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Icter=W())), salience=1)
  def sintoma29(self):
    self.declare(Fact(Icter="Si")) if "Ictericia" in lista_sintomas else self.declare(Fact(Icter="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Inqui=W())), salience=1)
  def sintoma30(self):
    self.declare(Fact(Inqui="Si")) if "Inquietud" in lista_sintomas else self.declare(Fact(Inqui="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Irrit=W())), salience=1)
  def sintoma31(self):
    self.declare(Fact(Irrit="Si")) if "Irritabilidad" in lista_sintomas else self.declare(Fact(Irrit="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Mal_Al=W())), salience=1)
  def sintoma32(self):
    self.declare(Fact(Mal_Al="Si")) if "Mal aliento" in lista_sintomas else self.declare(Fact(Mal_Al="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Mas_Ham=W())), salience=1)
  def sintoma33(self):
    self.declare(Fact(Mas_Ham="Si")) if "Más Hambre" in lista_sintomas else self.declare(Fact(Mas_Ham="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Moq=W())), salience=1)
  def sintoma34(self):
    self.declare(Fact(Moq="Si")) if "Moqueo" in lista_sintomas else self.declare(Fact(Moq="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Nau=W())), salience=1)
  def sintoma35(self):
    self.declare(Fact(Nau="Si")) if "Nausea" in lista_sintomas else self.declare(Fact(Nau="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Nec_Ori=W())), salience=1)
  def sintoma36(self):
    self.declare(Fact(Nec_Ori="Si")) if "Necesidad de orinar con frecuencia" in lista_sintomas else self.declare(Fact(Nec_Ori="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Nerv=W())), salience=1)
  def sintoma37(self):
    self.declare(Fact(Nerv="Si")) if "Nerviosismo" in lista_sintomas else self.declare(Fact(Nerv="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Or_Sang=W())), salience=1)
  def sintoma38(self):
    self.declare(Fact(Or_Sang="Si")) if "Orina con sangre" in lista_sintomas else self.declare(Fact(Or_Sang="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Or_Tur=W())), salience=1)
  def sintoma39(self):
    self.declare(Fact(Or_Tur="Si")) if "Orina turbia con olor desagradable" in lista_sintomas else self.declare(Fact(Or_Tur="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Per_Olf=W())), salience=1)
  def sintoma40(self):
    self.declare(Fact(Per_Olf="Si")) if "Perdida de olfato" in lista_sintomas else self.declare(Fact(Per_Olf="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Per_Pes=W())), salience=1)
  def sintoma41(self):
    self.declare(Fact(Per_Pes="Si")) if "Perdida de peso" in lista_sintomas else self.declare(Fact(Per_Pes="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Per_Gus=W())), salience=1)
  def sintoma42(self):
    self.declare(Fact(Per_Gus="Si")) if "Perdida del gusto" in lista_sintomas else self.declare(Fact(Per_Gus="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Piel_S=W())), salience=1)
  def sintoma43(self):
    self.declare(Fact(Piel_S="Si")) if "Piel seca" in lista_sintomas else self.declare(Fact(Piel_S="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Preoc=W())), salience=1)
  def sintoma44(self):
    self.declare(Fact(Preoc="Si")) if "Preocupación" in lista_sintomas else self.declare(Fact(Preoc="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Prob_Sue=W())), salience=1)
  def sintoma45(self):
    self.declare(Fact(Prob_Sue="Si")) if "Problemas de sueño" in lista_sintomas else self.declare(Fact(Prob_Sue="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Prob_Mem=W())), salience=1)
  def sintoma46(self):
    self.declare(Fact(Prob_Mem="Si")) if "Problemas de memoria" in lista_sintomas else self.declare(Fact(Prob_Mem="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Sen_Cal=W())), salience=1)
  def sintoma47(self):
    self.declare(Fact(Sen_Cal="Si")) if "Sensibilidad al calor" in lista_sintomas else self.declare(Fact(Sen_Cal="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Sen_Fri=W())), salience=1)
  def sintoma48(self):
    self.declare(Fact(Sen_Fri="Si")) if "Sensibilidad al frío" in lista_sintomas else self.declare(Fact(Sen_Fri="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Sib_Res=W())), salience=1)
  def sintoma49(self):
    self.declare(Fact(Sib_Res="Si")) if "Sibilancia al respirar" in lista_sintomas else self.declare(Fact(Sib_Res="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Sud=W())), salience=1)
  def sintoma50(self):
    self.declare(Fact(Sud="Si")) if "Sudoración" in lista_sintomas else self.declare(Fact(Sud="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Temp_Baj=W())), salience=1)
  def sintoma51(self):
    self.declare(Fact(Temp_Baj="Si")) if "Temperatura corporal baja" in lista_sintomas else self.declare(Fact(Temp_Baj="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Tos=W())), salience=1)
  def sintoma52(self):
    self.declare(Fact(Tos="Si")) if "Tos" in lista_sintomas else self.declare(Fact(Tos="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Tos_F=W())), salience=1)
  def sintoma53(self):
    self.declare(Fact(Tos_F="Si")) if "Tos con flema" in lista_sintomas else self.declare(Fact(Tos_F="No"))

  @Rule(Fact(action="Buscando enfermedad"), NOT(Fact(Vom=W())), salience=1)
  def sintoma54(self):
    self.declare(Fact(Vom="Si")) if "Vómito" in lista_sintomas else self.declare(Fact(Vom="No"))


  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="Si"),
        Fact(Dif_res="No"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="Si"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="No"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="No"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="Si"), Fact(Falt_Con="No"), Fact(Fatig="No"), Fact(Fieb="Si"),
        Fact(Flatu="Si"), Fact(Hec_Col="No"), Fact(Hinc_Abd="Si"), Fact(Icter="No"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="Si"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="No"), Fact(Tos_F="No"), Fact(Vom="Si"))
  def definirEnfermedad1(self):
    self.declare(Fact(enfermedad="Apendicitis"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="No"),
        Fact(Dif_res="No"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="No"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="No"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="No"), Fact(Falt_Con="No"), Fact(Fatig="No"), Fact(Fieb="No"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="No"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="No"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="No"), Fact(Tos_F="No"), Fact(Vom="No"))
  def definirEnfermedad2(self):
    self.declare(Fact(enfermedad="Apendicitis"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="No"),
        Fact(Dif_res="No"), Fact(Dol_Abd="Si"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="No"), Fact(Dol_Esp="No"), Fact(Dol_Hom="Si"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="No"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="Si"), Fact(Falt_Con="No"), Fact(Fatig="No"), Fact(Fieb="Si"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="Si"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="Si"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="No"), Fact(Tos_F="No"), Fact(Vom="Si"))
  def definirEnfermedad2(self):
    self.declare(Fact(enfermedad="Colelitiasis"))


  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="Si"), Fact(Diarr="No"),
        Fact(Dif_res="Si"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="No"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="Si"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="Si"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="No"), Fact(Falt_Con="No"), Fact(Fatig="Si"), Fact(Fieb="Si"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="No"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="Si"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="Si"), Fact(Tos="No"), Fact(Tos_F="Si"), Fact(Vom="Si"))
  def definirEnfermedad3(self):
    self.declare(Fact(enfermedad="Neumonía"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="Si"),
        Fact(Dif_res="No"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="Si"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="Si"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="No"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="No"), Fact(Falt_Con="No"), Fact(Fatig="No"), Fact(Fieb="Si"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="No"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="Si"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="No"), Fact(Tos_F="No"), Fact(Vom="Si"))
  def definirEnfermedad4(self):
    self.declare(Fact(enfermedad="Gastroenteritis"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="No"),
        Fact(Dif_res="No"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="No"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="Si"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="No"),
        Fact(Falt_Air="Si"), Fact(Falt_Ape="No"), Fact(Falt_Con="No"), Fact(Fatig="No"), Fact(Fieb="No"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="No"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="No"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="Si"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="Si"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="Si"), Fact(Tos_F="No"), Fact(Vom="No"))
  def definirEnfermedad5(self):
    self.declare(Fact(enfermedad="Asma"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="No"),
        Fact(Dif_res="No"), Fact(Dol_Abd="Si"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="Si"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="No"), Fact(Dol_Esp="Si"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="Si"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="No"), Fact(Falt_Con="No"), Fact(Fatig="No"), Fact(Fieb="Si"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="No"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="Si"),
        Fact(Nec_Ori="Si"), Fact(Nerv="No"), Fact(Or_Sang="Si"), Fact(Or_Tur="Si"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="No"), Fact(Tos_F="No"), Fact(Vom="Si"))
  def definirEnfermedad6(self):
    self.declare(Fact(enfermedad="Infección renal"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="No"),
        Fact(Dif_res="No"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="No"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="No"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="No"), Fact(Falt_Con="Si"), Fact(Fatig="No"), Fact(Fieb="No"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="No"), Fact(Inqui="Si"),
        Fact(Irrit="Si"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="No"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="Si"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="No"), Fact(Tos_F="No"), Fact(Vom="No"))
  def definirEnfermedad7(self):
    self.declare(Fact(enfermedad="Trastorno de ansiedad"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="No"),
        Fact(Dif_res="No"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="Si"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="Si"), Fact(Dol_Cab="No"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="No"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="Si"), Fact(Falt_Con="No"), Fact(Fatig="Si"), Fact(Fieb="Si"),
        Fact(Flatu="No"), Fact(Hec_Col="Si"), Fact(Hinc_Abd="No"), Fact(Icter="Si"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="Si"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="No"), Fact(Tos_F="No"), Fact(Vom="Si"))
  def definirEnfermedad8(self):
    self.declare(Fact(enfermedad="Hepatitis"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="Si"), Fact(Deb_Mus="Si"), Fact(Dep="Si"), Fact(Desor="No"), Fact(Diarr="No"),
        Fact(Dif_res="No"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="No"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="No"), Fact(Dol_Mus="Si"), Fact(Dol_Car="No"), Fact(Escal="No"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="No"), Fact(Falt_Con="No"), Fact(Fatig="Si"), Fact(Fieb="No"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="No"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="No"), Fact(Moq="No"), Fact(Nau="No"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="No"), Fact(Per_Gus="No"), Fact(Piel_S="Si"), Fact(Preoc="No"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="Si"), Fact(Sen_Cal="No"), Fact(Sen_Fri="Si"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="No"), Fact(Tos_F="No"), Fact(Vom="No"))
  def definirEnfermedad9(self):
    self.declare(Fact(enfermedad="Hipotiroidismo"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="Si"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="No"),
        Fact(Dif_res="No"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="No"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="No"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="No"), Fact(Escal="No"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="No"), Fact(Falt_Con="No"), Fact(Fatig="Si"), Fact(Fieb="No"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="No"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="No"), Fact(Mas_Ham="Si"), Fact(Moq="No"), Fact(Nau="No"),
        Fact(Nec_Ori="No"), Fact(Nerv="Si"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="No"),
        Fact(Per_Pes="Si"), Fact(Per_Gus="No"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="Si"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="Si"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="Si"),
        Fact(Temp_Baj="No"), Fact(Tos="No"), Fact(Tos_F="No"), Fact(Vom="No"))
  def definirEnfermedad10(self):
    self.declare(Fact(enfermedad="Hipertiroidismo"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes="No"), Fact(Deb_Mus="No"), Fact(Dep="No"), Fact(Desor="No"), Fact(Diarr="No"),
        Fact(Dif_res="No"), Fact(Dol_Abd="No"), Fact(Dol_Abd_inf="No"), Fact(Dol_Abd_sup="No"), Fact(Dol_Ori="No"),
        Fact(Dol_Art="No"), Fact(Dol_Cab="Si"), Fact(Dol_Esp="No"), Fact(Dol_Hom="No"), Fact(Dol_Oid="Si"),
        Fact(Dol_Pec="No"), Fact(Dol_Est="No"), Fact(Dol_Mus="No"), Fact(Dol_Car="Si"), Fact(Escal="No"),
        Fact(Falt_Air="No"), Fact(Falt_Ape="No"), Fact(Falt_Con="No"), Fact(Fatig="No"), Fact(Fieb="No"),
        Fact(Flatu="No"), Fact(Hec_Col="No"), Fact(Hinc_Abd="No"), Fact(Icter="No"), Fact(Inqui="No"),
        Fact(Irrit="No"), Fact(Mal_Al="Si"), Fact(Mas_Ham="No"), Fact(Moq="Si"), Fact(Nau="No"),
        Fact(Nec_Ori="No"), Fact(Nerv="No"), Fact(Or_Sang="No"), Fact(Or_Tur="No"), Fact(Per_Olf="Si"),
        Fact(Per_Pes="No"), Fact(Per_Gus="Si"), Fact(Piel_S="No"), Fact(Preoc="No"), Fact(Prob_Sue="No"),
        Fact(Prob_Mem="No"), Fact(Sen_Cal="No"), Fact(Sen_Fri="No"), Fact(Sib_Res="No"), Fact(Sud="No"),
        Fact(Temp_Baj="No"), Fact(Tos="Si"), Fact(Tos_F="No"), Fact(Vom="No"))
  def definirEnfermedad11(self):
    self.declare(Fact(enfermedad="Sinusitis"))

  @Rule(Fact(action="Buscando enfermedad"), Fact(enfermedad=MATCH.enfermedad), salience= -997)
  def asignarEnfermedad(self, enfermedad):
    self.enf=enfermedad
    self.confianza="1"

  @Rule(Fact(action="Buscando enfermedad"), Fact(Aum_Pes=MATCH.Aum_Pes), Fact(Deb_Mus=MATCH.Deb_Mus), Fact(Dep=MATCH.Dep), Fact(Desor=MATCH.Desor), Fact(Diarr=MATCH.Diarr),
        Fact(Dif_res=MATCH.Dif_res), Fact(Dol_Abd=MATCH.Dol_Abd), Fact(Dol_Abd_inf=MATCH.Dol_Abd_inf), Fact(Dol_Abd_sup=MATCH.Dol_Abd_sup), Fact(Dol_Ori=MATCH.Dol_Ori),
        Fact(Dol_Art=MATCH.Dol_Art), Fact(Dol_Cab=MATCH.Dol_Cab), Fact(Dol_Esp=MATCH.Dol_Esp), Fact(Dol_Hom=MATCH.Dol_Hom), Fact(Dol_Oid=MATCH.Dol_Oid),
        Fact(Dol_Pec=MATCH.Dol_Pec), Fact(Dol_Est=MATCH.Dol_Est), Fact(Dol_Mus=MATCH.Dol_Mus), Fact(Dol_Car=MATCH.Dol_Car), Fact(Escal=MATCH.Escal),
        Fact(Falt_Air=MATCH.Falt_Air), Fact(Falt_Ape=MATCH.Falt_Ape), Fact(Falt_Con=MATCH.Falt_Con), Fact(Fatig=MATCH.Fatig), Fact(Fieb=MATCH.Fieb),
        Fact(Flatu=MATCH.Flatu), Fact(Hec_Col=MATCH.Hec_Col), Fact(Hinc_Abd=MATCH.Hinc_Abd), Fact(Icter=MATCH.Icter), Fact(Inqui=MATCH.Inqui),
        Fact(Irrit=MATCH.Irrit), Fact(Mal_Al=MATCH.Mal_Al), Fact(Mas_Ham=MATCH.Mas_Ham), Fact(Moq=MATCH.Moq), Fact(Nau=MATCH.Nau),
        Fact(Nec_Ori=MATCH.Nec_Ori), Fact(Nerv=MATCH.Nerv), Fact(Or_Sang=MATCH.Or_Sang), Fact(Or_Tur=MATCH.Or_Tur), Fact(Per_Olf=MATCH.Per_Olf),
        Fact(Per_Pes=MATCH.Per_Pes), Fact(Per_Gus=MATCH.Per_Gus), Fact(Piel_S=MATCH.Piel_S), Fact(Preoc=MATCH.Preoc), Fact(Prob_Sue=MATCH.Prob_Sue),
        Fact(Prob_Mem=MATCH.Prob_Mem), Fact(Sen_Cal=MATCH.Sen_Cal), Fact(Sen_Fri=MATCH.Sen_Fri), Fact(Sib_Res=MATCH.Sib_Res), Fact(Sud=MATCH.Sud),
        Fact(Temp_Baj=MATCH.Temp_Baj), Fact(Tos=MATCH.Tos), Fact(Tos_F=MATCH.Tos_F), Fact(Vom=MATCH.Vom),
        NOT(Fact(enfermedad=MATCH.enfermedad)), salience=-999)
  def noEncontrada(self, Aum_Pes, Deb_Mus, Dep, Desor, Diarr, Dif_res, Dol_Abd, Dol_Abd_inf, Dol_Abd_sup, Dol_Ori, Dol_Art, Dol_Cab, Dol_Esp, Dol_Hom, Dol_Oid,
                   Dol_Pec, Dol_Est, Dol_Mus, Dol_Car, Escal, Falt_Air, Falt_Ape, Falt_Con, Fatig, Fieb, Flatu, Hec_Col, Hinc_Abd, Icter, Inqui, Irrit, Mal_Al,
                   Mas_Ham, Moq, Nau, Nec_Ori, Nerv, Or_Sang, Or_Tur, Per_Olf, Per_Pes, Per_Gus, Piel_S, Preoc, Prob_Sue, Prob_Mem, Sen_Cal, Sen_Fri, Sib_Res,
                   Sud, Temp_Baj, Tos, Tos_F, Vom):
    listaSintomasPresentados= [Aum_Pes, Deb_Mus, Dep, Desor, Diarr, Dif_res, Dol_Abd, Dol_Abd_inf, Dol_Abd_sup, Dol_Ori, Dol_Art, Dol_Cab, Dol_Esp, Dol_Hom, Dol_Oid,
                   Dol_Pec, Dol_Est, Dol_Mus, Dol_Car, Escal, Falt_Air, Falt_Ape, Falt_Con, Fatig, Fieb, Flatu, Hec_Col, Hinc_Abd, Icter, Inqui, Irrit, Mal_Al,
                   Mas_Ham, Moq, Nau, Nec_Ori, Nerv, Or_Sang, Or_Tur, Per_Olf, Per_Pes, Per_Gus, Piel_S, Preoc, Prob_Mem, Prob_Sue, Sen_Cal, Sen_Fri, Sib_Res,
                   Sud, Temp_Baj, Tos, Tos_F, Vom]
    cuenta_maxima_sintomas= 0
    enfermedad_relacionada = ""
    for key,val in mapa_sintomas.items():
      cont=0
      lista_temp = eval(key)
      for i in range(0, len(listaSintomasPresentados)):
        if(lista_temp[i] == listaSintomasPresentados[i] and listaSintomasPresentados[i] == "Si"):
          cont = cont + 1
      if cont > cuenta_maxima_sintomas:
        cuenta_maxima_sintomas = cont
        enfermedad_relacionada = val
    self.enf = enfermedad_relacionada
    self.confianza="0"

