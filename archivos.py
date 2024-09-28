/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package laboratorio1;

import java.util.Scanner;

/**
 *
 * @author ASUS
 */
public class Laboratorio1 {
    private static Peliculas pelicula=new Peliculas("pelis.txt");
    private static Clientes cliente=new Clientes("clientes.txt"); 
    private static Compras compra=new Compras("Compras.txt");
    public static Scanner read=new Scanner(System.in);

    public static void main(String[] args) {
        pelicula.agregarPelicula(1,"batman","nolan",2008,"accion",30);
        pelicula.agregarPelicula(2,"Poor things","desconocido",2023,"drama",12);
        pelicula.agregarPelicula(3,"Dune 2","directo",2024,"accion",70);
        pelicula.agregarPelicula(4,"whale","Arronofsky",2022,"drama",90);
        pelicula.mostrarPeli();
        System.out.println("clientes");
        cliente.agregarCliente(12, "Alex", "alex@gmai.com", "Betania");
        cliente.agregarCliente(22, "April", "april@gmai.com", "Villa campestre");
        cliente.agregarCliente(32, "Wendy", "Wendy@gmai.com", "Miramar");
        cliente.agregarCliente(42, "Jake", "Jake@gmai.com", "Villa Carolina");
        cliente.mostrarCliente();
        System.out.println("Compras");
        compra.agregarCompra(55, 12, 1, "6 agosto");
        compra.agregarCompra(56, 22, 2, "6 agosto");
        compra.agregarCompra(57, 32, 3, "6 agosto");
        compra.agregarCompra(58, 42, 4, "6 agosto");
        compra.mostrarCompra();
        
        // TODO code application logic here
    }
    
}

package laboratorio1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/**
 *
 * @author ASUS
 */
public class Peliculas {
    private String ruta;
    
    public Peliculas(String ruta){
        this.ruta=ruta;
}
    public void agregarPelicula(int id_peli,String titulo,String director,int año,String genero,float precio){
        if(idExiste(id_peli)){
            System.out.println("la peliculla esta registrada.");
        }else{
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(ruta,true))){
                writer.write(id_peli+","+titulo+","+director+","+año+","+genero+","+precio+"\n");
            
            }catch(IOException e){
                System.out.println("error."+e.getMessage());
            }
        }
    }
    
    public boolean idExiste(int id_peli){
        try (BufferedReader reader = new BufferedReader(new FileReader(ruta))){
            String linea;
            while((linea = reader.readLine()) != null){
                String[] partes = linea.split(",");
                if (Integer.parseInt(partes[0]) == id_peli) {
                    return true;
                }
                
            }
            
        }catch(IOException e){
            System.out.println("error al leer"+e.getMessage());
        
        }
        return false;
    
    }
    public void mostrarPeli(){
        try (BufferedReader reader = new BufferedReader(new FileReader(ruta))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                String[] partes = linea.split(",");
                System.out.println("ID: " + partes[0] + ", Titulo: " + partes[1] + ", director: " + partes[2]+",año:"+ partes[3]+",genero"+partes[4]+",precio"+partes[5]);
                
            }
        }catch(IOException e){
            System.out.println("ERROR"+e.getMessage());
        
        }
    }
    
    
    
}

package laboratorio1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Compras {
    private String ruta;
    public Compras(String ruta){
        this.ruta=ruta;
    }
    public void agregarCompra(int id_compra,int id_cliente,int id_peli,String fecha){
        if(idcomExiste(id_cliente)){
            System.out.println("la compra.");
        }else{
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(ruta,true))){
                writer.write(id_compra+","+id_cliente+","+id_peli+","+fecha+"\n");
            
            }catch(IOException e){
                System.out.println("error."+e.getMessage());
            }
        }
    }
    public boolean idcomExiste(int id_cliente){
        try (BufferedReader reader = new BufferedReader(new FileReader(ruta))){
            String linea;
            while((linea = reader.readLine()) != null){
                String[] partes = linea.split(",");
                if (Integer.parseInt(partes[0]) == id_cliente) {
                    return true;
                }
                
            }
            
        }catch(IOException e){
            System.out.println("error al leer"+e.getMessage());
        
        }
        return false;
    
    }
    public void mostrarCompra(){
        try (BufferedReader reader = new BufferedReader(new FileReader(ruta))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                String[] partes = linea.split(",");
                System.out.println("ID: " + partes[0] + ", ID_cliente: " + partes[1] + ", ID_correo: " + partes[2]+",Fecha:"+ partes[3]);
                
            }
        }catch(IOException e){
            System.out.println("ERROR"+e.getMessage());
        
        }
    }
    
}

package laboratorio1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Clientes {
    private String ruta;
    public Clientes(String ruta){
        this.ruta=ruta;
    }
    public void agregarCliente(int id_cliente,String nombre,String correo,String direccion){
        if(idcExiste(id_cliente)){
            System.out.println("el cliente.");
        }else{
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(ruta,true))){
                writer.write(id_cliente+","+nombre+","+correo+","+direccion+"\n");
            
            }catch(IOException e){
                System.out.println("error."+e.getMessage());
            }
        }
    }
    public boolean idcExiste(int id_cliente){
        try (BufferedReader reader = new BufferedReader(new FileReader(ruta))){
            String linea;
            while((linea = reader.readLine()) != null){
                String[] partes = linea.split(",");
                if (Integer.parseInt(partes[0]) == id_cliente) {
                    return true;
                }
                
            }
            
        }catch(IOException e){
            System.out.println("error al leer"+e.getMessage());
        
        }
        return false;
    
    }
    public void mostrarCliente(){
        try (BufferedReader reader = new BufferedReader(new FileReader(ruta))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                String[] partes = linea.split(",");
                System.out.println("ID: " + partes[0] + ", Nombre: " + partes[1] + ", correo: " + partes[2]+",direccion:"+ partes[3]);
                
            }
        }catch(IOException e){
            System.out.println("ERROR"+e.getMessage());
        
        }
    }
}
