# Importer les bibliothèques nécessaires
import streamlit as st 
import streamlit.components.v1 as components 

# STYLE + SLIDESHOW (images qui défilent en fond)
st.markdown("""
    <style>
    /* Rendre le fond transparent pour voir les images */
    .stApp {
        background-color: transparent !important;
    }
    
    /* Positionner les images du slideshow en arrière-plan */
    .slideshow {
        position: fixed;  /* Reste fixe quand on scroll */
        top: 0;
        left: 0;
        width: 100%;  /* Prend toute la largeur */
        height: 100%;  /* Prend toute la hauteur */
        z-index: -1;  /* En arrière-plan (derrière tout le reste) */
    }
    
    /* Chaque image du slideshow */
    .slideshow img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;  /* Couvre tout sans déformer */
        opacity: 0;  /* Invisible au départ */
        transition: opacity 2s ease-in-out;  /* Transition douce en 2 secondes */
    }
    
    /* L'image "active" */
    .slideshow img.active {
        opacity: 0.5; 
    }
    </style>
    
    <!-- Les 3 images qui vont défiler -->
    <div class="slideshow">
        <img class="active" src="https://tse1.mm.bing.net/th/id/OIP.hk2-2cNkm1B1dgzOqjz5EgHaE7?r=0&cb=thfvnextfalcon&rs=1&pid=ImgDetMain&o=7&rm=3">
        <img src="https://image.shutterstock.com/image-photo/thai-travel-tourism-concept-design-260nw-236406352.jpg">
        <img src="https://www.destination-asie.com/wp-content/uploads/2023/07/24-meilleurs-endroits-pour-voyager-en-asie-2-0.jpg">
    </div>
""", unsafe_allow_html=True)

# JAVASCRIPT (faire défiler les images automatiquement)
components.html("""
    <script>
    setTimeout(() => {  /* Attendre 1 seconde avant de commencer */
        const imgs = window.parent.document.querySelectorAll('.slideshow img');  /* Trouver toutes les images */
        let i = 0;  /* Compteur: quelle image afficher */
        setInterval(() => {  /* Répéter chaque 3 secondes */
            imgs[i].classList.remove('active');  /* Masquer l'image actuelle */
            i = (i + 1) % imgs.length;  /* Passer à l'image suivante */
            imgs[i].classList.add('active');  /* Afficher la nouvelle image */
        }, 3000);  /* 3000 millisecondes = 3 secondes */
    }, 1000);
    </script>
""", height=0)

# TITRE CENTRÉ AVEC BELLE POLICE
st.markdown("<h1 style='text-align: center; font-family: Playfair Display;'>Voyages ✈️🗺️</h1>", unsafe_allow_html=True)

# BIENVENUE CENTRÉ
st.markdown("<h2 style='text-align: center;'>Bienvenue !</h2>", unsafe_allow_html=True)

# MENU DANS LA BARRE À GAUCHE (SIDEBAR)
page = st.sidebar.selectbox(" Menu", ["Accueil", "Destinations"])

# PAGE ACCUEIL
if page == "Accueil":
    st.markdown("<h2 style='text-align: center; font-family: Playfair Display; font-size: 2.5em;'>Découvre des destinations de rêve 🌍</h2>", unsafe_allow_html=True)

# PAGE DESTINATIONS
elif page == "Destinations":
    # Dropdown pour choisir une destination
    destination = st.selectbox("Choisis une destination", ["Japon", "Chine", "Vietnam", "L'ile de la Reunion", "Polynésie française"])
    
    # Dictionnaire = tableau contenant les images pour chaque destination
    images = {
        "Japon": [
            "https://i.pinimg.com/736x/52/47/76/524776e534164dec237246050f9be415.jpg",
            "https://unsacsurledos.com/wp-content/uploads/2024/11/hakone-japon-1536x1028.jpg",
            "https://cdn-imgix.headout.com/media/images/3cea8adb3e7f3ca6e15a3a40a06e3653-Osaka%20Castle%203.jpg"
        ],
        "Chine": [
            "https://img.freepik.com/photos-premium/vue-aerienne-grande-muraille-chine-monument-emblematique-s-etendant-vaste-paysage-grande-muraille-chine-dans-brume-longue-vue-surrealiste-partir-photographie-par-drone-generee-par-ia_538213-17939.jpg",
            "https://www.finance-investissement.com/wp-content/uploads/sites/2/2018/08/efired_123rf_50972728_custom.jpg",
            "https://i.pinimg.com/736x/95/d6/fe/95d6fe4636b9a04053da1e5159704d63.jpg"
        ],
        "Vietnam": [
            "https://localvietnam.nl/wp-content/uploads/2024/05/y-linh-ho-rijstvelden-sapa-1.jpg",
            "https://th.bing.com/th/id/R.747949e64394f7520a8aea2cf0e41531?rik=Uh1RiEcRFrWcqQ&riu=http%3a%2f%2fadmin.vn-tourism.com%2fIMAGE_MANAGER_CACHE_PATH%2ff5%2ff5a7d3_lantern-a.jpg&ehk=E0SM7gi07jVlYSqgSitY%2fk%2bplZKrDSdxdiBXF3Y0X1A%3d&risl=&pid=ImgRaw&r=0",
            "https://vilandtravel.com/files/images/2024/07/golden-bridge-ba-na-hills.jpg"
        ],
        "L'ile de la Reunion": [
            "https://cdn.generationvoyage.fr/2024/03/Vue-sur-la-ville-du-cirque-de-Cilaos-La-Reunion.jpeg",
            "https://static.actu.fr/uploads/2025/10/capture-decran-2025-10-10-103304-960x640.png",
            "https://www.atterrir.com/wp-content/uploads/2016/09/Cascade-Langevin-Sud-Sauvage.jpeg"
        ],
        "Polynésie française": [
            "https://img.freepik.com/photos-premium/plage-tropicale-palmier-scene-plage_1085346-69961.jpg",
            "https://blog.vivre-en-polynesie.com/wp-content/uploads/2025/01/Les-principales-iles-de-la-Polynesie-francaise-3.jpg",
            "https://foundtheworld.com/wp-content/uploads/2016/01/Tahiti-French-Polynesia-7.jpg"
        ]
    }
    
    # Récupérer les 3 images de la destination choisie
    imgs = images.get(destination, [])
    
    # Créer une boîte HTML avec les 3 images
    html_images = f"""
    <div style="background-color: rgba(255, 255, 255, 0.3); padding: 30px; border-radius: 10px; margin: 20px; display: flex; gap: 20px;">
        <img src="{imgs[0]}" style="width: 32%; border-radius: 8px;">
        <img src="{imgs[1]}" style="width: 32%; border-radius: 8px;">
        <img src="{imgs[2]}" style="width: 32%; border-radius: 8px;">
    </div>
    """
    
    # Afficher la boîte HTML
    st.markdown(html_images, unsafe_allow_html=True)
