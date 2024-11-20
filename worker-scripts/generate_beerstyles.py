array1 = [
    ["1A", "American Light Lager", "Standard American Beer", "A highly carbonated, light-bodied, and mild-flavored lager."],
    ["1B", "American Lager", "Standard American Beer", "A clean and crisp pale lager with minimal bitterness."],
    ["1C", "Cream Ale", "Standard American Beer", "A smooth and mildly fruity ale with a clean finish."],
    ["1D", "American Wheat Beer", "Standard American Beer", "A refreshing beer with prominent wheat flavors and light hoppiness."],
    ["2A", "International Pale Lager", "International Lager", "A balanced pale lager with mild malt and hop character."],
    ["2B", "International Amber Lager", "International Lager", "A malt-forward lager with amber hues and a smooth finish."],
    ["2C", "International Dark Lager", "International Lager", "A dark lager with subtle caramel and roasted malt notes."],
    ["3A", "Czech Pale Lager", "Czech Lager", "A light-bodied lager with floral hop aroma and mild bitterness."],
    ["3B", "Czech Premium Pale Lager", "Czech Lager", "A richer pale lager with a balance of malt sweetness and hop bitterness."],
    ["3C", "Czech Amber Lager", "Czech Lager", "A medium-bodied lager with toasty malt and light caramel flavors."],
    ["3D", "Czech Dark Lager", "Czech Lager", "A dark lager with chocolate and coffee-like malt flavors."],
    ["4A", "Munich Helles", "Pale Malty European Lager", "A soft and malty lager with a touch of sweetness."],
    ["4B", "Festbier", "Pale Malty European Lager", "A golden lager with rich malt character and smooth drinkability."],
    ["4C", "Helles Bock", "Pale Malty European Lager", "A strong pale lager with robust malt flavors and light hop bitterness."],
    ["5A", "German Leichtbier", "Pale Bitter European Beer", "A low-alcohol beer with crisp flavors and subtle hoppiness."],
    ["5B", "Kölsch", "Pale Bitter European Beer", "A clean and delicately balanced beer with fruity esters."],
    ["5C", "German Helles Exportbier", "Pale Bitter European Beer", "A stronger pale lager with malty sweetness and moderate hops."],
    ["5D", "German Pils", "Pale Bitter European Beer", "A dry and crisp lager with pronounced hop bitterness."],
    ["6A", "Märzen", "Amber Malty European Lager", "A medium-bodied amber lager with toasty malt flavors."],
    ["6B", "Rauchbier", "Amber Malty European Lager", "A smoky lager with notes of beechwood-smoked malt."],
    ["6C", "Dunkles Bock", "Amber Malty European Lager", "A strong amber lager with rich malt flavors and a smooth finish."],
    ["7A", "Vienna Lager", "Amber Bitter European Beer", "A copper-colored lager with toasty malt and light hop bitterness."],
    ["7B", "Altbier", "Amber Bitter European Beer", "A German ale with a malty backbone and moderate hop presence."],
    ["7C", "Kellerbier: Amber Kellerbier", "Amber Bitter European Beer", "An unfiltered amber lager with a fresh and malty taste."],
    ["7C", "Kellerbier: Pale Kellerbier", "Amber Bitter European Beer", "An unfiltered pale lager with a crisp and clean finish."],
    ["8A", "Munich Dunkel", "Dark European Lager", "A smooth dark lager with rich malt flavors and a clean finish."],
    ["8B", "Schwarzbier", "Dark European Lager", "A dark lager with subtle roasted malt and light bitterness."],
    ["9A", "Doppelbock", "Strong European Beer", "A strong and malty beer with caramel and dark fruit flavors."],
    ["9B", "Eisbock", "Strong European Beer", "A highly concentrated beer with intense malt sweetness."],
    ["9C", "Baltic Porter", "Strong European Beer", "A smooth and robust dark beer with caramel and chocolate notes."],
    ["10A", "Weissbier", "German Wheat Beer", "A refreshing wheat beer with banana and clove flavors."],
    ["10B", "Dunkles Weissbier", "German Wheat Beer", "A dark wheat beer with caramel and banana notes."],
    ["10C", "Weizenbock", "German Wheat Beer", "A strong wheat beer with rich malt and fruity flavors."],
    ["11A", "Ordinary Bitter", "British Bitter", "A sessionable ale with a balance of malt sweetness and hop bitterness."],
    ["11B", "Best Bitter", "British Bitter", "A flavorful ale with a malty backbone and assertive bitterness."],
    ["11C", "Strong Bitter", "British Bitter", "A strong ale with complex malt flavors and a hoppy finish."],
    ["12A", "British Golden Ale", "Pale Commonwealth Beer", "A light and crisp ale with a touch of fruity sweetness."],
    ["12B", "Australian Sparkling Ale", "Pale Commonwealth Beer", "A refreshing ale with a dry finish and fruity esters."],
    ["12C", "English IPA", "Pale Commonwealth Beer", "A hoppy ale with earthy and floral notes."],
    ["13A", "Dark Mild", "Brown British Beer", "A low-alcohol dark ale with caramel and toffee flavors."],
    ["13B", "British Brown Ale", "Brown British Beer", "A malty ale with nutty and chocolate flavors."],
    ["13C", "English Porter", "Brown British Beer", "A dark ale with roasted malt and light chocolate notes."],
    ["14A", "Scottish Light", "Scottish Ale", "A light-bodied ale with sweet malt and low bitterness."],
    ["14B", "Scottish Heavy", "Scottish Ale", "A medium-bodied ale with caramel malt flavors."],
    ["14C", "Scottish Export", "Scottish Ale", "A rich and malty ale with a clean finish."],
    ["15A", "Irish Red Ale", "Irish Beer", "A malt-forward ale with caramel and toasty flavors."],
    ["15B", "Irish Stout", "Irish Beer", "A dry and roasty stout with coffee and chocolate notes."],
    ["15C", "Irish Extra Stout", "Irish Beer", "A strong and robust stout with dark chocolate flavors."],
    ["16A", "Sweet Stout", "Dark British Beer", "A creamy stout with a sweet malt character."],
    ["16B", "Oatmeal Stout", "Dark British Beer", "A smooth stout with a silky mouthfeel and roasted malt flavors."],
    ["16C", "Tropical Stout", "Dark British Beer", "A sweet and fruity stout with dark malt flavors."],
    ["16D", "Foreign Extra Stout", "Dark British Beer", "A strong and bold stout with roasted and fruity notes."],
    ["17A", "British Strong Ale", "Strong British Ale", "A rich and malty ale with complex flavors."],
    ["17B", "Old Ale", "Strong British Ale", "A dark and full-bodied ale with caramel and toffee notes."],
    ["17C", "Wee Heavy", "Strong British Ale", "A strong Scotch ale with sweet and malty flavors."],
    ["17D", "English Barleywine", "Strong British Ale", "A strong and rich ale with toffee and dried fruit notes."],
    ["18A", "Blonde Ale", "Pale American Ale", "A light and easy-drinking ale with mild malt and hops."],
    ["18B", "American Pale Ale", "Pale American Ale", "A hoppy pale ale with citrus and pine notes."],
    ["19A", "American Amber Ale", "Amber and Brown American Beer", "A malty amber ale with caramel and toasty flavors."],
    ["19B", "California Common", "Amber and Brown American Beer", "A hybrid beer with toasty malt and earthy hops."],
    ["19C", "American Brown Ale", "Amber and Brown American Beer", "A brown ale with nutty and chocolate malt flavors."],
    ["20A", "American Porter", "American Porter and Stout", "A dark beer with roasted malt and chocolate flavors."],
    ["20B", "American Stout", "American Porter and Stout", "A bold stout with roasted malt and coffee notes."],
    ["20C", "Imperial Stout", "American Porter and Stout", "A strong stout with rich chocolate and dark fruit flavors."],
    ["21A", "American IPA", "IPA", "A hoppy and aromatic ale with citrus and pine notes."]]

array2 = [["21B","Belgian IPA", "Specialty IPA", "A Belgian-style IPA with fruity esters and hop bitterness."],
    ["21B", "Black IPA", "Specialty IPA", "A dark IPA with roasted malt and bold hop character."],
    ["21B", "Brown IPA", "Specialty IPA", "A malt-forward IPA with hints of caramel and chocolate."],
    ["21B", "Brut IPA", "Specialty IPA", "A dry and effervescent IPA with a crisp finish."],
    ["21B", "Red IPA", "Specialty IPA", "An IPA with bold hop character and a malty red hue."],
    ["21B", "Rye IPA", "Specialty IPA", "An IPA with spicy rye malt and prominent hop bitterness."],
    ["21B", "White IPA", "Specialty IPA", "A wheat-based IPA with fruity and citrusy notes."],
    ["21C", "Hazy IPA", "IPA", "A juicy and cloudy IPA with tropical and citrus flavors."],
    ["22A", "Double IPA", "Strong American Ale", "A strong and intensely hoppy IPA with high bitterness."],
    ["22B", "American Strong Ale", "Strong American Ale", "A bold ale with a high ABV and rich malt character."],
    ["22C", "American Barleywine", "Strong American Ale", "A strong and malty ale with caramel and fruity notes."],
    ["22D", "Wheatwine", "Strong American Ale", "A strong ale with prominent wheat and sweet malt flavors."],
    ["23A", "Berliner Weisse", "European Sour Ale", "A tart and refreshing wheat beer with a low ABV."],
    ["23B", "Flanders Red Ale", "European Sour Ale", "A complex sour ale with red fruit and oak notes."],
    ["23C", "Oud Bruin", "European Sour Ale", "A dark sour ale with caramel and fruity acidity."],
    ["23D", "Lambic", "European Sour Ale", "A traditional Belgian sour ale with wild yeast character."],
    ["23E", "Gueuze", "European Sour Ale", "A blend of young and old lambics with a tart flavor."],
    ["23F", "Fruit Lambic", "European Sour Ale", "A lambic infused with fresh fruit for a sweet and sour taste."],
    ["23G", "Gose", "European Sour Ale", "A tart and salty wheat beer with coriander notes."],
    ["24A", "Witbier", "Belgian Ale", "A Belgian wheat beer with spices like coriander and orange peel."],
    ["24B", "Belgian Pale Ale", "Belgian Ale", "A balanced ale with malt sweetness and light hop bitterness."],
    ["24C", "Bière de Garde", "Belgian Ale", "A French farmhouse ale with malt complexity and earthy notes."],
    ["25A", "Belgian Blond Ale", "Strong Belgian Ale", "A light and fruity ale with subtle malt sweetness."],
    ["25B", "Saison", "Strong Belgian Ale", "A dry and spicy farmhouse ale with fruity esters."],
    ["25C", "Belgian Golden Strong Ale", "Strong Belgian Ale", "A strong and effervescent ale with fruity and spicy notes."],
    ["26A", "Belgian Single", "Monastic Ale", "A light and crisp ale brewed in monastic tradition."],
    ["26B", "Belgian Dubbel", "Monastic Ale", "A rich and malty ale with dark fruit and caramel flavors."],
    ["26C", "Belgian Tripel", "Monastic Ale", "A strong and pale ale with fruity esters and spicy phenols."],
    ["26D", "Belgian Dark Strong Ale", "Monastic Ale", "A complex ale with dark fruit, caramel, and malty richness."],
    ["27A", "Historical Beer: Gose", "Historical Beer", "A historical sour wheat beer with salt and coriander."],
    ["27A", "Historical Beer: Kellerbier", "Historical Beer", "An unfiltered and fresh lager with a natural taste."],
    ["27A", "Historical Beer: Kentucky Common", "Historical Beer", "An American beer with corn adjuncts and mild hop character."],
    ["27A", "Historical Beer: Lichtenhainer", "Historical Beer", "A smoky sour wheat beer with a unique tartness."],
    ["27A", "Historical Beer: London Brown Ale", "Historical Beer", "A sweet brown ale with low ABV and caramel flavors."],
    ["27A", "Historical Beer: Piwo Grodziskie", "Historical Beer", "A Polish smoked wheat beer with a light body."],
    ["27A", "Historical Beer: Pre-Prohibition Lager", "Historical Beer", "A robust American lager with a malty backbone."],
    ["27A", "Historical Beer: Pre-Prohibition Porter", "Historical Beer", "A dark porter with roasted malt and historical roots."],
    ["27A", "Historical Beer: Roggenbier", "Historical Beer", "A German rye beer with spicy and bready flavors."],
    ["27A", "Historical Beer: Sahti", "Historical Beer", "A Finnish farmhouse ale with juniper and malt character."],
    ["28A", "Brett Beer", "American Wild Ale", "A wild ale fermented with Brettanomyces yeast for funky flavors."],
    ["28B", "Mixed-Fermentation Sour Beer", "American Wild Ale", "A sour ale with complex flavors from mixed fermentation."],
    ["28C", "Wild Specialty Beer", "American Wild Ale", "A wild ale with unique ingredients and bold flavors."],
    ["28D", "Straight Sour Beer", "American Wild Ale", "A clean and tart sour beer with a refreshing finish."],
    ["29A", "Fruit Beer", "Fruit Beer", "A beer brewed with fruit for added sweetness and flavor."],
    ["29B", "Fruit and Spice Beer", "Fruit Beer", "A beer with added fruit and spices for a complex taste."],
    ["29C", "Specialty Fruit Beer", "Fruit Beer", "A fruit beer with unique brewing techniques or ingredients."],
    ["29D", "Grape Ale", "Fruit Beer", "A beer brewed with grapes for a wine-like character."],
    ["30A", "Spice, Herb, or Vegetable Beer", "Spiced Beer", "A beer brewed with spices, herbs, or vegetables for unique flavors."],
    ["30B", "Autumn Seasonal Beer", "Spiced Beer", "A seasonal beer with fall spices like cinnamon and nutmeg."],
    ["30C", "Winter Seasonal Beer", "Spiced Beer", "A warming seasonal beer with spices like clove and ginger."],
    ["30D", "Specialty Spice Beer", "Spiced Beer", "A spiced beer with innovative or non-traditional ingredients."]]


# use extend because in theory it only extends the first array, while the
# '+'-operator creates a new list; uses less memory with extend()
array1.extend(array2)

print("Extended array1:", array1)
