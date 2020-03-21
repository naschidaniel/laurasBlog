import axios from "axios";
import store from "@/store";
export async function api(apiLink) {
  try {
    const response = await axios.get(apiLink);
    if (response.status == 200) {
      const data = await response.data;
      store.dispatch("setAlertError", "None", false);
      return data;
    } else {
      store.dispatch("setAlertError", "StatusError", response.status);
    }
  } catch (error) {
    store.dispatch("setAlertError", "Error", error);
  }
}
