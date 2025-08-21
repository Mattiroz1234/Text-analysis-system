from dal import get_tweets
from processor import Analyzer



def analysis():
    data = get_tweets()
    results = []

    for _, row in data.iterrows():
        tweet_df = row.to_frame().T
        analyzer = Analyzer(tweet_df)

        result = {
            "id": row["id"],
            "text": row["Text"],
            "rarest_word": analyzer.finding_the_rarest_word(),
            "emotion": analyzer.finding_the_emotion(),
            "weapons": analyzer.finding_weapons()
        }
        results.append(result)

    return results







