import axios from "axios";

export async function getBlogPosts() {
    try {
      const response = await axios.get("/api/blogposts/?format=json");
      const data = await response.data;
      return data
    } catch (error) {
      console.log(error);
    }
  }