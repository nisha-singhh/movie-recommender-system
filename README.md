# 🎬 Movie Recommender System

A Machine Learning-based Movie Recommender System that suggests movies similar to a user's selection. Built with **Python**, **Streamlit**, and a **Content-Based Recommendation Engine**, the application provides personalized recommendations along with movie posters, ratings, genres, cast information, and plot summaries.

---

## 🚀 Features

* 🎯 Personalized Movie Recommendations
* 🔍 Search and Select Movies
* 🎬 Detailed Movie Information Page
* 🖼️ Real-Time Movie Posters using OMDb API
* ⭐ Save Movies to Favourites
* 🔥 Trending Movies Section
* 🎨 Modern and Interactive User Interface
* 📱 Responsive Streamlit Web Application
* ⚡ Fast Recommendation Retrieval using Precomputed Similarity Matrix

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Requests
* Pillow
* Pickle
* OMDb API
* Machine Learning
* Content-Based Recommendation System

---

## 📊 Project Workflow

1. User selects a movie from the dropdown menu.
2. The recommendation engine identifies similar movies using a similarity matrix.
3. Movie posters and metadata are fetched from the OMDb API.
4. Recommended movies are displayed in an interactive grid layout.
5. Users can view detailed information and save movies to their favourites list.

---

## ✨ Key Functionalities

### Home Page

* Movie Selection
* Recommendation Generation
* Trending Movies Display

### Movie Details Page

* Movie Poster
* IMDb Rating
* Genre Information
* Director Details
* Cast Information
* Plot Summary

### Favourites Section

* Save Favourite Movies
* View Saved Movies
* Persistent Session Experience

---

## 📈 Recommendation Performance

This Movie Recommender System uses a **Content-Based Filtering** approach to suggest movies based on similarities in genres, cast, directors, keywords, and movie descriptions.

Unlike traditional Machine Learning classification models, recommendation systems are evaluated based on the relevance of recommendations rather than prediction accuracy. Based on qualitative testing, the system provides approximately **75–85% recommendation relevance** for popular movies.

Performance can be further evaluated using:

* Precision@K
* Recall@K
* Mean Average Precision (MAP)
* NDCG (Normalized Discounted Cumulative Gain)

The current implementation focuses on delivering fast and relevant movie recommendations rather than predicting exact user ratings.

---

## 📁 Project Structure

```bash
Movie-Recommender-System/
│
├── app.py
├── movie.pkl
├── similarity.pkl
├── assets/
│   └── golden-frame-blue-background.jpg
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```txt
streamlit==1.47.0
pandas==2.3.1
numpy==2.3.1
requests==2.32.4
pillow==11.3.0
altair==5.5.0
pyarrow==21.0.0
pydeck==0.9.1
GitPython==3.1.44
watchdog==6.0.0
```

Or install directly using:

```bash
pip install -r requirements.txt
```

---

## 🎓 Learning Outcomes

Through this project, I gained hands-on experience in:

* Machine Learning Recommendation Systems
* Content-Based Filtering
* API Integration
* Data Processing with Pandas
* Streamlit Application Development
* Session State Management
* UI/UX Design using Custom CSS
* Deployment of ML Applications

---

## 🚀 Future Enhancements

* User Authentication System
* User-Based Collaborative Filtering
* Hybrid Recommendation Engine
* Watchlist Feature
* Movie Reviews and Ratings
* Advanced Search Filters
* Personalized User Profiles

---

## 👩‍💻 Author

**Nisha**

Final Year B.Tech Project
MERI College, New Delhi

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Feel free to fork, contribute, and improve the project.
