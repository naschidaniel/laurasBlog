import axios from "axios";

export async function api(apiLink) {
  try {
    const response = await axios.get(apiLink);
    const data = await response.data;
    return data
  } catch (error) {
      console.log(error);
  }
}