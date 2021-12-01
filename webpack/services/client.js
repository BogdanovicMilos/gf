import axios from "axios";

const client = axios.create({
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken"
});

client.interceptors.response.use(
  response => response.data,
  error => {
    return Promise.reject(error);
  }
);

export default client;
