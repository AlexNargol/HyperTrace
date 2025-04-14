use sysinfo::{System};
use telemetry::{MemoryInfo, DistroInfo};
use tonic::{Request, Response, Status};
// use tonic_reflection::server::{Builder as ReflectionBuilder};
use std::net::SocketAddr;
use tonic::transport::Server;
use crate::telemetry::telemetry_service_server::TelemetryService;
use crate::telemetry::{MemoryRequest, DistroRequest};


pub mod telemetry {
    tonic::include_proto!("telemetry"); // matches `package telemetry;` in .proto
}

#[derive(Default)]
pub struct MyTelemetryService;

#[tonic::async_trait]
impl TelemetryService for MyTelemetryService {
    // Handle sending MemoryInfo
    async fn send_memory_info(
        &self,
        request: Request<MemoryRequest>,
    ) -> Result<Response<MemoryInfo>, Status> {

        // Create a new System instance to fetch system information
        let mut system = System::new_all();
        system.refresh_all();
        
        // Extract MemoryInfo from the request
        let _memory_info = request.into_inner();

        // Assume we're fetching actual memory data from the system or using some method
        let free_memory: u64 = system.available_memory();
        let used_memory: u64 = system.used_memory();
        let total_memory: u64 = system.total_memory();

       
        // Now create the MemoryInfo struct and assign the values to it
        let reply = MemoryInfo {
            free_memory: free_memory as f32,
            used_memory: used_memory as f32,
            total_memory: total_memory as f32,
        };
    
        // Print out the received memory info for debugging
        println!("Received MemoryInfo: {:?}", reply);

        // Send a response back with the status message
        Ok(Response::new(reply))

    }


    // Handle sending DistroInfo
    async fn send_distro_info(
        &self,
        _request: Request<DistroRequest>, // Expect Empty for the request
    ) -> Result<Response<DistroInfo>, Status> {        

        // Create a new System instance to fetch system information
        //let _System = System::new_all();

        // Assume we're fetching actual distro data from the system or using some method
        let distro = System::distribution_id();
        let cpu_arch = System::cpu_arch();
        let core_count: i32 = match System::physical_core_count() { 
            Some(cores) => cores.try_into().unwrap_or(0), // Try to convert usize to i32
            None => 0, // Default to 0 if core count is unavailable
        };
        let distro_ver = System::long_os_version().expect("Failed to get OS version");

        // Now create the DistroInfo struct and assign the values to it
        let reply = DistroInfo {
            distro,
            cpu_arch,
            core_count,
            distro_ver,
        };

        // Print out the received distro info for debugging
        println!("Received DistroInfo: {:?}", reply);

        // Send a response back with the status message
        Ok(Response::new(reply))
    }
}


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr: SocketAddr = "127.0.0.1:8000".parse()?;
    let greeter = MyTelemetryService::default();

    println!("Server listening on {}", addr);

    Server::builder()
        .add_service(crate::telemetry::telemetry_service_server::TelemetryServiceServer::new(greeter))
        .serve(addr)
        .await?;

    Ok(())
}