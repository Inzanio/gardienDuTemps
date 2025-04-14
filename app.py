import streamlit as st
from datetime import date
from babel.dates import format_date

# Définir la locale en français



st.set_page_config(
    layout="wide",
    page_title="Gardien Du Temps",
    page_icon="👮🏻🚨",
)

st.title("👮🏻:blue[Gardien] du :green[temps]⏳")

col1, col2 = st.columns(2)

start_date = date(2025, 3, 17) #col1.date_input("Date de début", value=date(2025, 3, 13),format="DD/MM/YYYY")
end_date = date(2025, 8, 16)#col2.date_input("Date de fin", value=date(2025, 8, 16),format="DD/MM/YYYY")
col1.metric(f"🚩Date Début",value=f"{format_date(start_date,locale='fr_FR')}")
col2.metric(f"🏁Date de Fin",value=f"{format_date(end_date,locale='fr_FR')}")
# Calculer la différence entre les deux dates
delta = end_date - start_date

# Extraire le nombre de jours de l'objet timedelta
days = delta.days

today = date.today()

# Afficher le temps total prévu en jours
st.subheader(f"Temps total Prévu : :green[{days} jours]")

if start_date > end_date:
    st.error("La date de début ne peut pas être après la date de fin.")
else:
    # Calculer la différence entre aujourd'hui et la date de début
    delta_debut = today - start_date
    jours_ecoules = delta_debut.days

    # Calculer la différence entre la date de fin et aujourd'hui
    delta_fin = end_date - today
    jours_restants = delta_fin.days + 1

    col1,col2 = st.columns(2)
    # Afficher les résultats
    col1.metric(f"⏳Temps Ecoulés⏳",value=f"{jours_ecoules} Jours")
    col2.metric(f"⏰Temps Restants⏰",value=f"{jours_restants} Jours")
    st.metric(f"➡️Avancement➡️",value=f"{(jours_ecoules / (end_date - start_date).days) * 100 if (end_date - start_date).days != 0 else 0:.2f}%")