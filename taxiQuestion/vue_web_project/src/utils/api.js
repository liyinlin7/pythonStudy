// Axios 的安装 npm install axios
import axios from 'axios'  // 导入axios库

// axios 全局默认配置
// axios.defaults.baseURL = 'http://120.27.146.185:8076/api'
// axios.defaults.baseURL = 'http://124.223.33.41:8076/api'
axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.defaults.validateStatus = (status) => { return status >= 200 && status < 400 }
axios.defaults.withCredentials = true
document.cookie = 'csrftoken=VDxqKsO49WaQR3RMc30ICLOWTe3ivH4wpGyvzTgv4Qjm02qJFvWfDLsG5aIiSjBg'
document.cookie = 'sessionid=tj8dyg0rcshhgcgj6wka1dtuql0djw3f'

export const postResquest = (url, data, head) => {
    return axios.post(url, data)
}

export const deleteResquest = (url, params) => {
    return axios.delete(url, { params })
}

export const putResquest = (url, data) => {
    return axios.put(url, data)
}

export const getResquest = (url, params) => {
    return axios.get(url, { params })
}
