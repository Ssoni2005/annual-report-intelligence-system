import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const here=path.dirname(fileURLToPath(import.meta.url));
const root=process.env.ARIS_DATA_DIR?path.resolve(process.env.ARIS_DATA_DIR):path.resolve(here,'../../../data');
const paths={demo:'demo.json',foundation:'foundation.json',intake:'intake.json',parsing:'parsing.json',chunking:'chunking.json',structures:'structures.json'} as const;
function read(name:keyof typeof paths){return JSON.parse(fs.readFileSync(path.join(root,paths[name]),'utf8'));}
function write(name:keyof typeof paths,data:unknown){const target=path.join(root,paths[name]);const tmp=target+'.tmp';fs.writeFileSync(tmp,JSON.stringify(data,null,2));fs.renameSync(tmp,target);}
export const readStore=()=>read('demo'); export const writeStore=(d:unknown)=>write('demo',d);
export const readFoundation=()=>read('foundation'); export const writeFoundation=(d:unknown)=>write('foundation',d);
export const readIntake=()=>read('intake'); export const writeIntake=(d:unknown)=>write('intake',d);
export const readParsing=()=>read('parsing'); export const writeParsing=(d:unknown)=>write('parsing',d);
export const readChunking=()=>read('chunking'); export const writeChunking=(d:unknown)=>write('chunking',d);
export function snapshotStructure(note='Manual snapshot',actor='System'){const main=readStore(),f=readFoundation(),s=f.structures[0];s.version+=1;s.updatedAt=new Date().toISOString();s.updatedBy=actor;f.versions.unshift({id:`v${s.version}-${Date.now()}`,structureId:s.id,version:s.version,createdAt:s.updatedAt,createdBy:actor,note,headingCount:main.headings.length,snapshot:structuredClone(main.headings)});writeFoundation(f);return s.version;}
export function audit(actor:string,action:string,target:string,detail:string){const f=readFoundation();f.auditLogs.unshift({id:`a-${Date.now()}-${Math.random().toString(36).slice(2,7)}`,time:new Date().toISOString(),actor,action,target,detail});writeFoundation(f);}

export const readStructures=()=>read('structures'); export const writeStructures=(d:unknown)=>write('structures',d);
