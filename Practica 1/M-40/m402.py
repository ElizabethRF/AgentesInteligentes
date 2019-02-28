import urllib.request as ur
import re 

f = ur.urlopen('http://infocar.dgt.es/etraffic/Incidencias?ca=13&provIci=&caracter=acontecimiento&accion_consultar=Consultar&IncidenciasRETENCION=IncidenciasRETENCION&IncidenciasPUERTOS=IncidenciasPUERTOS&IncidenciasMETEOROLOGICA=IncidenciasMETEOROLOGICA&IncidenciasEVENTOS=IncidenciasEVENTOS&IncidenciasOTROS=IncidenciasOTROS&IncidenciasRESTRICCIONES=IncidenciasRESTRICCIONES&ordenacion=fechahora_ini-DESC')
s = f.read().decode()
f.close()

print(s)

conjuntoPrueba = re.findall("<tr.*?<td.*?class='orange'>(\d\d:\d\d).*?(\d\d/\d\d/\d\d\d\d).*?<td.*?class='orange'>(\d\d:\d\d)*.*?(\d\d/\d\d/\d\d\d\d)*.*?<td.*?<td.*?<td.*?<b>(.*?)</b>.*?<td.*?<span.*?<b>(.*?)</b></span>.*?</td>.*?",variable,re.DOTALL)
print(conjuntoPrueba)