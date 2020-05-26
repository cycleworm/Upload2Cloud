using System;
using System.IO;
using WixSharp;

class Script
{
    static public void Main()
    {
        var project = new Project("SendToSkynet",
                          new Dir(@"%ProgramFiles%\\SkynetApplications\\SendToSkynet",
                              new WixSharp.File("dist\\upload.ico"),
                              new WixSharp.File("dist\\sendToSkynet.exe")),
                              //new Dir(@"%Desktop%",
                              new Dir(@"%AppData%/Microsoft/Windows/SendTo",
                                new ExeFileShortcut("- Upload to Skynet", Path.Combine("[INSTALLDIR]", "sendToSkynet.exe"), arguments: "") { WorkingDirectory = "[INSTALLDIR]" })
                              );



        project.GUID = new Guid("6f330b47-2577-43ad-9095-1761ba25889d");

        Compiler.BuildMsi(project);
    }
}
/*
 new Dir("INSTALLDIR",
  new Files(Path.Combine(BuildDir, "*.*")),
  new Dir(@"%Desktop%",
    new ExeFileShortcut(AppNameWithVersion, Path.Combine("[INSTALLDIR]", $"{BuildSettings.ApplicationName}.exe"), arguments: "") { WorkingDirectory = "[INSTALLDIR]" }),
  new Dir(@"%ProgramMenu%",
    new ExeFileShortcut(AppNameWithVersion, Path.Combine("[INSTALLDIR]", $"{BuildSettings.ApplicationName}.exe"), arguments: "") { WorkingDirectory = "[INSTALLDIR]" }))



        "C:\Program Files (x86)\SkynetApplications\SendToSkynet\{BuildSettings.ApplicationName}.exe"

        "C:\Program Files (x86)\SkynetApplications\SendToSkynet\"

        C:\Users\aukreisa\PycharmProjects\SendToSkynet\dist\sendToSkynet.exe

        C:\Users\aukreisa\PycharmProjects\SendToSkynet\dist

        "C:\Program Files (x86)\SkynetApplications\SendToSkynet\sendToSkynet.exe"
        "C:\Program Files (x86)\SkynetApplications\SendToSkynet"
        */