import "../styles/globals.css";
import "../styles/NavBar.component.css";

async function getCollection(name: string, expand = "") {
  expand = `expand=${expand}&` || "";
  const res = await fetch(
    `http://127.0.0.1:8090/api/collections/${name}/records?${expand}page=1&perPage=30`
  );
  const data = await res.json();
  return data?.items as any[];
}

function MenuItem({ item }: any) {
  const { key, name } = item || {};

  // TODO item should open search with clicked item as search param

  return (
    <li key={key}>
      <a href="#">{name}</a>
    </li>
  );
}

export default async function Navbar() {
  const flavors = await getCollection("flavors");
  const meals = await getCollection("meals");
  const ingredients = await getCollection("ingredient_groups", "ingredients");
  const diets = await getCollection("diets");

  return (
    <nav className="navbar">
      <ul>
        <li>
          <a href="#">RCPSTAK</a>
        </li>
        <li>
          <a href="#">Flavors</a>
          <ul>
            {flavors?.map((item) => {
              return <MenuItem key={item.id} item={item} />;
            })}
          </ul>
        </li>
        <li>
          <a href="#">Meals</a>
          <ul>
            {meals?.map((item) => {
              return <MenuItem key={item.id} item={item} />;
            })}
          </ul>
        </li>
        <li>
          <a href="#">Ingredients</a>
          <ul>
            {ingredients?.map((item) => {
              return (
                <li key={item.key}>
                  <a href="#">{item.name}</a>
                  {"@expand" in item && (
                    <ul>
                      {item["@expand"].ingredients?.map((ingredient: any) => {
                        return (
                          <li key={ingredient.key}>
                            <a href="#">{ingredient.name}</a>
                          </li>
                        );
                      })}
                    </ul>
                  )}
                </li>
              );
            })}
          </ul>
        </li>
        <li>
          <a href="#">Diets</a>
          <ul>
            {diets?.map((item) => {
              return <MenuItem key={item.id} item={item} />;
            })}
          </ul>
        </li>
        {/* TODO add CSS darkmode toggle */}
        {/* TODO implement login system */}
        <li>
          <a href="#">Sign In</a>
        </li>
      </ul>
    </nav>
  );
}
