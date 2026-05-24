using System;
using System.Collections;
using UnityEngine;
using UnityEngine.Networking;

public class TestPython : MonoBehaviour
{
    [System.Serializable]
    public class Test
    {
        public string title;

        public Test(string title)
        {
            this.title = title;
        }
    }
    private void Start()
    {
        StartCoroutine(GetText());
    }

    private IEnumerator GetText()
    {
        string id = "18vfbpEUDMCO6SDPVQl8QoMBk489zCTX43JtCtNc4mHE";
        string name = "Literary_Lockdown_Data";
        UnityWebRequest result = UnityWebRequest.Get($"http://127.0.0.1:8000/sheets/{id}/{name}");
        yield return result.SendWebRequest();
        
        if (result.result != UnityWebRequest.Result.Success) Debug.Log(result.error);
        else Debug.Log(result.downloadHandler.text);
    }
    
    private IEnumerator CreateEntry(string json)
    {
        UnityWebRequest result = UnityWebRequest.Post($"http://127.0.0.1:8000/postTodo", "POST"); // Create request
        
        byte[] jsonRaw = System.Text.Encoding.UTF8.GetBytes(json); // Converting to bytes
        
        result.uploadHandler = new UploadHandlerRaw(jsonRaw); // Create body
        result.downloadHandler = new DownloadHandlerBuffer(); // Store callback
        result.SetRequestHeader("Content-Type", "application/json"); // Sets content type header (Specifies request type)
        
        yield return result.SendWebRequest(); // Sends request
        
        if (result.result != UnityWebRequest.Result.Success) Debug.Log(result.error);
        else Debug.Log(result.downloadHandler.text);
        Debug.Log("Sending data");
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.A)) StartCoroutine(CreateEntry(JsonUtility.ToJson(new Test("test"), true)));
    }
}
