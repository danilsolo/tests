querry = '''
CREATE TABLE profiles(
    id integer PRIMARY KEY,
    username text default null,
    heroflag text default null,
    heroname text default null,
    prof text default null,
    attack integer default 0,
    defense integer default 0,
    exp integer default 0,
    stamina integer default 0,
    gold integer default 0,
    gems integer default 0,
    wins integer default 0,
    sword text default null,
    dagger text default null,
    head text default null,
    arms text default null,
    body text default null,
    legs text default null,
    specials text default null,
    stock integer default 0,
    pet text default null
)'''