import axios from "axios";

export async function getBlogCategories() {
  try {
    const response = await axios.get("/api/blogcategories/?format=json")
    const data = await response.data;
    return data
  } catch (error) {
    console.log(error);
  }
}