import axios from "axios";

export async function getPages(link) {
  try {
    const response = await axios.get("/api/pages/" + link + "/?format=json");
    const data = await response.data;
    return data
  } catch (error) {
      console.log(error);
  }
}