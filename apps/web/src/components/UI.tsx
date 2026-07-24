import React from 'react';
export const Card=({children,className=''}:{children:React.ReactNode,className?:string})=><div className={'card '+className}>{children}</div>;
export const Badge=({children,tone='blue'}:{children:React.ReactNode,tone?:string})=><span className={'badge '+tone}>{children}</span>;
export const Button=({children,variant='primary',onClick,disabled=false,type='button'}:{children:React.ReactNode;variant?:string;onClick?:()=>void;disabled?:boolean;type?:'button'|'submit'})=><button type={type} disabled={disabled} className={'btn '+variant} onClick={onClick}>{children}</button>;
export const Modal=({title,children,onClose,width='680px'}:{title:string;children:React.ReactNode;onClose:()=>void;width?:string})=><div className="overlay" onMouseDown={e=>{if(e.target===e.currentTarget)onClose()}}><div className="modal" style={{width:`min(${width},95vw)`}}><div className="modalHead"><h3>{title}</h3><button onClick={onClose}>×</button></div>{children}</div></div>;
export const EmptyState=({title,detail}:{title:string;detail:string})=><div className="emptyState"><b>{title}</b><p>{detail}</p></div>;
