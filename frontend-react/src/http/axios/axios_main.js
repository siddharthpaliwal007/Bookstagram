import axios from 'axios';

const token = localStorage.getItem('userToken');

const axiosMain = axios.create({
  baseURL: 'http://40.80.95.65/store',
  headers: {
    // 'Content-Type': 'application/json',
    'Authorization': "token " + token,
  },
});
export default axiosMain;
