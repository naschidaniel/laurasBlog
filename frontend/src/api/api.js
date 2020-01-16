import axios from "axios";

export async function api(apiLink) {
  try {
    const response = await axios.get(apiLink);
    if (response.status == 200) {
      const data = await response.data;
      return data;
    } else {
      console.log("Api Status: " + response.status);
    }
  } catch (error) {
    console.log(error);
  }
}
