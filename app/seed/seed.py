# create info for the database here
from app import db
from app.models import Drink, Cocktail

if __name__ == '__main__':
    budlight = Drink(drID=1,
                     Brand='Anheuser-Busch',
                     Supply=900,
                     Type='Beer',
                     Name='BudLight'
                     )

    yuengling = Drink(drID=2,
                      Brand='Yuengling',
                      Supply=900,
                      Type='Beer',
                      Name='Yuengling'
                      )

    budweiser = Drink(drID=3,
                      Brand='Anheuser-Busch',
                      Supply=900,
                      Type='Beer',
                      Name='Budweiser'
                      )

    guinness = Drink(drID=4,
                     Brand='Diageo',
                     Supply=900,
                     Type='Beer',
                     Name='Guinness'
                     )

    dos_equis = Drink(drID=5,
                      Brand='Heineken',
                      Supply=900,
                      Type='Beer',
                      Name='Dos Equis'
                      )

    shiner_bock = Drink(drID=6,
                        Brand='The Gambrinus Company',
                        Supply=900,
                        Type='Beer',
                        Name='Shiner Bock'
                        )

    lagavulin_16 = Drink(drID=7,
                         Brand='Diageo',
                         Supply=240,
                         Type='Scotch',
                         Name='Lagavulin 16'
                         )

    woodford_reserve = Drink(drID=8,
                             Brand='the Brown-Forman Corporation',
                             Supply=240,
                             Type='Bourbon',
                             Name='Woodford Reserve'
                             )

    michters_rye = Drink(drID=9,
                         Brand='Joe Magliocco',
                         Supply=240,
                         Type='Rye',
                         Name='Michters Rye'
                         )

    bombay_sapphire = Drink(drID=10,
                            Brand='Bacardi',
                            Supply=240,
                            Type='Gin',
                            Name='Bombay Sapphire'
                            )

    havana_club = Drink(drID=11,
                        Brand='Corporación Cuba Ron',
                        Supply=240,
                        Type='Rum',
                        Name='Havana Club'
                        )

    titos = Drink(drID=12,
                  Brand='Bert Beveridge',
                  Supply=240,
                  Type='Vodka',
                  Name='Titos'
                  )

    db.session.add(budlight)
    db.session.add(yuengling)
    db.session.add(budweiser)
    db.session.add(guinness)
    db.session.add(dos_equis)
    db.session.add(shiner_bock)
    db.session.add(lagavulin_16)
    db.session.add(woodford_reserve)
    db.session.add(michters_rye)
    db.session.add(bombay_sapphire)
    db.session.add(havana_club)
    db.session.add(titos)
    db.session.commit()

    budlight_bottle = Cocktail(ckID=1,
                               Name='BudLight',
                               Ratio="12",
                               Ingredients="budlight",
                               Price=4
                               )

    yuengling_bottle = Cocktail(ckID=2,
                                Name='Yuengling',
                                Ratio="12",
                                Ingredients="yuengling",
                                Price=4
                                )

    budweiser_bottle = Cocktail(ckID=3,
                                Name='Budweiser',
                                Ratio="12",
                                Ingredients="budweiser",
                                Price=4
                                )

    guinness_bottle = Cocktail(ckID=4,
                               Name='Guinness',
                               Ratio="12",
                               Ingredients="guinness",
                               Price=5
                               )

    dos_equis_bottle = Cocktail(ckID=5,
                                Name='Dos Equis',
                                Ratio="12",
                                Ingredients="dos equis",
                                Price=5
                                )

    shiner_bock_bottle = Cocktail(ckID=6,
                                  Name='Shiner Bock',
                                  Ratio="12",
                                  Ingredients="shiner bock",
                                  Price=5
                                  )

    lagavulin_16_neat = Cocktail(ckID=7,
                                 Name='Lagavulin 16 Neat',
                                 Ratio="2",
                                 Ingredients="lagavulin 16",
                                 Price=15
                                 )

    old_fashioned = Cocktail(ckID=8,
                             Name='Old Fashioned',
                             Ratio="2,0.25,0.05",
                             Ingredients="woodford reserve,simple,angostura",
                             Price=12
                             )

    manhattan = Cocktail(ckID=9,
                         Name='Manhattan',
                         Ratio="2,1,0.05",
                         Ingredients="michters rye,sweet_vermouth,angostura",
                         Price=12
                         )

    martini = Cocktail(ckID=10,
                       Name='Martini',
                       Ratio="2,1,0.05",
                       Ingredients="bombay sapphire,dry_vermouth,orange_bitters",
                       Price=11
                       )

    daiquiri = Cocktail(ckID=11,
                        Name='Daiquiri',
                        Ratio="2,.75,.75",
                        Ingredients="havana club,simple,lime_juice",
                        Price=10
                        )

    black_russian = Cocktail(ckID=12,
                             Name='Black russian',
                             Ratio="2,1",
                             Ingredients="titos,kahlua",
                             Price=10
                             )

    db.session.add(budlight_bottle)
    db.session.add(yuengling_bottle)
    db.session.add(budweiser_bottle)
    db.session.add(guinness_bottle)
    db.session.add(dos_equis_bottle)
    db.session.add(shiner_bock_bottle)
    db.session.add(lagavulin_16_neat)
    db.session.add(old_fashioned)
    db.session.add(manhattan)
    db.session.add(martini)
    db.session.add(daiquiri)
    db.session.add(black_russian)
    db.session.commit()
