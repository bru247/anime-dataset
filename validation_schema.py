from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

categorias_type = ['TV', 'Movie', 'OVA', 'Special', 'ONA']
categorias_status = ['Finished Airing', 'Currently Airing', 'Not yet aired']
categorias_season = ['spring', 'summer', 'fall', 'winter', 'UNKNOWN']

schema = DataFrameSchema(
    columns={
        "ANIME_ID": Column(
            dtype="int64",
            nullable=False,
            unique=True,
            required=True,
        ),
        "NAME": Column(
            dtype="object",
            nullable=False,
            required=True,
        ),
        "SCORE": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=10.0),
            ],
            nullable=False,
            unique=False,
            required=True,
        ),
        "TYPE": Column(
            dtype="object",
            checks=Check.isin(categorias_type),
            nullable=False,
            required=True,
        ),
        "EPISODES": Column(
            dtype="float64",
            nullable=False,
            required=True,
        ),
        "STATUS": Column(
            dtype="object",
            checks=Check.isin(categorias_status),
            nullable=False,
            required=True,
        ),
        "STUDIOS": Column(
            dtype="object",
            nullable=False,
            required=True,
        ),
        "SOURCE": Column(
            dtype="object",
            nullable=False,
            required=True,
        ),
        "RATING": Column(
            dtype="object",
            nullable=False,
            required=True,
        ),
        "RANK": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
            ],
            nullable=False,
            required=True,
        ),
        "POPULARITY": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
            ],
            nullable=False,
            required=True,
        ),
        "FAVORITES": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
            ],
            nullable=False,
            required=True,
        ),
        "SCORED_BY": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
            ],
            nullable=False,
            required=True,
        ),
        "MEMBERS": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
            ],
            nullable=False,
            required=True,
        ),
        "DURATION_FINAL": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
            ],
            nullable=False,
            required=True,
        ),
        "PREMIERED_SEASON": Column(
            dtype="object",
            checks=Check.isin(categorias_season),
            nullable=False,
            required=True,
        ),
        "PREMIERED_YEAR": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=1950.0),
                Check.less_than_or_equal_to(max_value=2025.0),
            ],
            nullable=True,
            required=True,
        ),
        "Action": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Adventure": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "AvantGarde": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "AwardWinning": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "BoysLove": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Comedy": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Drama": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Ecchi": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Erotica": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Fantasy": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "GirlsLove": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Gourmet": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Hentai": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Horror": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Mystery": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Romance": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Sci-Fi": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "SliceofLife": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Sports": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Supernatural": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
        "Suspense": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=1.0),
            ],
            nullable=False,
            required=True,
        ),
    },
    strict=True,
    ordered=True,
    unique_column_names=True,
)