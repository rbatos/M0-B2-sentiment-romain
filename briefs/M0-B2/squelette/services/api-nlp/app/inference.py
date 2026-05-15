"""Logique d'inférence pour la classification de sentiment.

Le modèle CamemBERT chargé sort des labels 5 étoiles
(`'1 star'`, `'2 stars'`, ..., `'5 stars'`). Le métier (Aubergine Hôtels)
veut 3 classes (`négatif`, `neutre`, `positif`).

→ Ton travail dans ce fichier :
   1. Implémenter `predict_sentiment()` (récupère scores 5★ + appelle map).
   2. Implémenter `map_stars_to_sentiment()` (mapping 5★ → 3 classes).
   3. Justifier le seuil retenu en commentaire (cf. brief).

Le pipeline transformers est chargé une seule fois au démarrage, dans
`main.py` (lifespan), et stocké dans `state["pipeline"]`. Tu le récupères
en argument.
"""
from __future__ import annotations

import time
from typing import Any

from app.schemas import Sentiment, SentimentOut


def map_stars_to_sentiment(star_label: str) -> Sentiment:
    """Mappe un label 5 étoiles ('1 star', ..., '5 stars') en 3 classes métier.

    À compléter par l'apprenant. Convention attendue (à justifier dans
    le README perso async) :
        1-2 stars -> 'négatif'
        3 stars   -> 'neutre'
        4-5 stars -> 'positif'

    Args:
        star_label: label produit par le modèle (ex: '4 stars').

    Returns:
        Sentiment 3 classes.

    Raises:
        ValueError: si `star_label` n'est pas dans le format attendu.
    """
    # TODO Tâche 3 — compléter ce mapping et justifier le seuil retenu
    # en commentaire (1-2 → négatif, 3 → neutre, 4-5 → positif par défaut).
    raise NotImplementedError("Compléter `map_stars_to_sentiment` (Tâche 3).")


def predict_sentiment(pipeline: Any, text: str, model_name: str) -> SentimentOut:
    """Inférence de sentiment sur un texte FR.

    Args:
        pipeline: pipeline `transformers.pipeline("text-classification", ...)`
            chargé au démarrage de l'API.
        text: texte FR de la review.
        model_name: identifiant HF du modèle (passé pour traçabilité).

    Returns:
        SentimentOut avec sentiment 3 classes, scores 5★ bruts, et latence ms.
    """
    # TODO Tâche 3 — compléter :
    #
    # 1. Mesurer le temps d'inférence (time.perf_counter() avant/après).
    # 2. Appeler `pipeline(text, top_k=None)` pour récupérer toutes les
    #    probabilités (5 entrées, une par étoile).
    # 3. Construire `scores_5_stars: dict[str, float]` à partir du résultat.
    # 4. Identifier le label argmax (la plus haute proba).
    # 5. Appeler `map_stars_to_sentiment(label_argmax)` pour obtenir la
    #    classe métier.
    # 6. Renvoyer un `SentimentOut(...)`.
    raise NotImplementedError("Compléter `predict_sentiment` (Tâche 3).")