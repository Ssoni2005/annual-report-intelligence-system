const API=(import.meta.env.VITE_API_URL||'http://localhost:4000/api').replace(/\/$/,'');
async function request<T>(path:string,options:RequestInit={}):Promise<T>{
  const r=await fetch(API+path,{...options,headers:{'Content-Type':'application/json','x-user-id':'u1','x-user-name':'Dr. Sitaram Soni',...(options.headers||{})}});
  if(!r.ok){const text=await r.text();let message=text||`Request failed (${r.status})`;try{message=JSON.parse(text).error||message}catch{}throw new Error(message)}
  if(r.status===204)return undefined as T;
  return r.json() as Promise<T>;
}
export const getJson=<T>(path:string)=>request<T>(path);
export const postJson=<T>(path:string,body:unknown)=>request<T>(path,{method:'POST',body:JSON.stringify(body)});
export const patchJson=<T>(path:string,body:unknown)=>request<T>(path,{method:'PATCH',body:JSON.stringify(body)});
export const deleteJson=<T>(path:string)=>request<T>(path,{method:'DELETE'});
export const sendJson=<T>(path:string,method:'POST'|'PATCH'|'PUT'|'DELETE',body?:unknown)=>request<T>(path,{method,body:body===undefined?undefined:JSON.stringify(body)});
