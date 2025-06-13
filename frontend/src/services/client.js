import axios from 'axios';

const client = axios.create({
    baseURL : ' http://localhost:8000/app/',
});

export default client;